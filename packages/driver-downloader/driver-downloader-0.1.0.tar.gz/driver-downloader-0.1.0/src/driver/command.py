from pathlib import Path
from typing import Optional
import typer
from typer import Option
from .core import downloader, driver_version

app = typer.Typer(name="chromedriver 同步")


@app.command()
def download(
    version: Optional[str] = Option(None, "--v", help="chromedriver版本"),
    save_path: Optional[Path] = Option(".", "--save", help="保存路径"),
):
    if version:
        downloader.download(version, save_path)
    else:
        downloader(save_path=save_path)
        version = driver_version(str(save_path / "chromedriver.exe"))
    typer.echo(
        f"Current Chromedriver({save_path / 'chromedriver.exe'}) Version: {version}"
    )


if __name__ == "__main__":
    app()
