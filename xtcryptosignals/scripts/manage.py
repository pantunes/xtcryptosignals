__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
import click
import subprocess
from shutil import copyfile


SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
CHOICES = (
    "copy-config-files",
    "start",
    "stop",
    "start-except-order-books",
    "start-order-books",
)


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument("operation", required=True, type=click.Choice(CHOICES))
def main(operation):
    if operation == CHOICES[0]:
        for x in (
            "client.prod.env",
            "server.prod.env",
            "client.dev.env",
            "server.dev.env",
            "client.docker.env",
            "server.docker.env",
        ):
            filepath_source = os.path.join(SCRIPT_PATH, "../config", x)
            filepath_dest = os.path.join(os.getcwd(), "config", x)
            try:
                copyfile(filepath_source, filepath_dest)
                click.echo(f"Copied from {filepath_source} to {filepath_dest}")
            except IOError:
                os.makedirs(os.path.dirname(filepath_dest))
                click.echo(f"Created folder {filepath_dest}")
                copyfile(filepath_source, filepath_dest)
                click.echo(f"Copied from {filepath_source} to {filepath_dest}")
        return

    i = CHOICES.index(operation)
    subprocess.call(f"sh {SCRIPT_PATH}/xt-{CHOICES[i]}.sh", shell=True)
