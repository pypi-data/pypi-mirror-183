import pathlib
import re
import subprocess
import winreg
import zipfile

import httpx


def chrome_version():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, r"SOFTWARE\Google\Chrome\BLBeacon"
        )
        value = winreg.QueryValueEx(key, "version")[0]
        if search := re.search(r"^[1-9]\d+(\.\d+){2}", value):
            return search.group()
        return None
    except WindowsError as e:
        return None


def driver_version(driver_path: str | None = None):
    if not driver_path:
        driver_path = "chromedriver"
    try:
        res = subprocess.check_output([driver_path, "--version"])
    except subprocess.CalledProcessError as e:
        return None
    except FileNotFoundError:
        return None
    else:
        return re.search(r"\d+\.\d+\.\d+", res.decode("utf-8")).group()


def find_versions(url):
    with httpx.Client() as client:
        response = client.get(url)
        for item in (item for item in response.json() if item["type"] == "dir"):
            yield item["name"]


def search_version(versions, chrome_v):
    for version in versions:
        if re.search(chrome_v, version):
            return version


def download_driver(url, save_path):
    temp_file = pathlib.Path("chrome_driver.zip")
    with open(temp_file, "wb") as fp:
        with httpx.stream(
            "GET",
            url,
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
            },
            follow_redirects=True,
        ) as response:
            for chunk in response.iter_bytes():
                fp.write(chunk)
    with zipfile.ZipFile("chrome_driver.zip", mode="r") as file:
        file.extractall(save_path, file.namelist())
    temp_file.unlink(missing_ok=True)
    if (path := (pathlib.Path(save_path) / "chromedriver.exe")).exists():
        return path


class DriverDownload:
    def __init__(self):
        self.version_url = "https://registry.npmmirror.com/-/binary/chromedriver/"
        self.driver_url = "https://registry.npmmirror.com/-/binary/chromedriver/{}chromedriver_win32.zip"

    def __call__(
        self, driver_path: str | None = None, save_path: str | pathlib.Path = "."
    ):
        chrome = chrome_version()
        if not chrome:
            raise FileNotFoundError("not find chrome.exe")
        if not (driver := driver_version(driver_path)) or driver != chrome:
            if version := search_version(find_versions(self.version_url), chrome):
                return download_driver(
                    self.driver_url.format(version), pathlib.Path(save_path)
                )
            raise ValueError(f"not find match (Chrome {chrome}) driver")

    def download(self, version: str, save_path: str | pathlib.Path = "."):
        return download_driver(self.driver_url.format(version), pathlib.Path(save_path))


downloader = DriverDownload()

__all__ = ["downloader", "DriverDownload", "driver_version"]
