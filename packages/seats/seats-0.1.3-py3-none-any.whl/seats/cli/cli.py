import click

from .cmdbs.group import cmdb
from .connectors.group import connector
from .notebooks.group import notebooks


@click.group()
def entry_point():
    """Security Engineering Automation Tool Set (SEATS)

    Collection of CLI commands using the seats package."""
    pass


# noinspection PyTypeChecker
entry_point.add_command(cmdb)
# noinspection PyTypeChecker
entry_point.add_command(connector)
# noinspection PyTypeChecker
entry_point.add_command(notebooks)
