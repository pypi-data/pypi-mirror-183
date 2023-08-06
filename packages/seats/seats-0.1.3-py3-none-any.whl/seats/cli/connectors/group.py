import click
from seats.connectors.fortigate.rest import FortigateREST


@click.group()
def connector():
    """Interact with devices and services using connectors"""
    pass


@connector.command()
@click.argument('hostname')
@click.argument('username')
@click.option("--password", prompt=True, hide_input=True)
def fortigate(hostname, username, password):
    """Use fortigate REST connector"""
    fgt = FortigateREST()
    fgt.hostname = hostname
    fgt.username = username
    fgt.password = password
    print(fgt)


