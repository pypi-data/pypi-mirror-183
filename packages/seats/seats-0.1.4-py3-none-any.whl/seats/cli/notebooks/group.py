import click
import site
from pathlib import Path


@click.group()
def notebooks():
    """Interact, Install or Update Jupyter notebooks """
    pass


@notebooks.command()
@click.argument('destination', type=click.Path())
def install(destination):
    """Install sample notebooks to home folder"""
    home = Path.home()
    print(home)
    print(Path(destination))
    for location in site.getsitepackages():
        path = Path(location)
        package_path = path / "seats"
        if package_path.is_dir():
            print(package_path)

