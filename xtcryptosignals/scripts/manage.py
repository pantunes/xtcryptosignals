__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
import click
import subprocess


SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))


@click.command(
    context_settings=dict(help_option_names=['-h', '--help'])
)
@click.argument(
    'operation', required=True, type=click.Choice(
        ['start', 'stop', 'restart']
    )
)
def main(operation):
    if operation == 'start':
        subprocess.call("sh {}/xt-start.sh".format(SCRIPT_PATH), shell=True)
    elif operation == 'stop':
        subprocess.call("sh {}/xt-stop.sh".format(SCRIPT_PATH), shell=True)
    else:
        subprocess.call("sh {}/xt-stop.sh ; sh {}/xt-start.sh".format(
            SCRIPT_PATH, SCRIPT_PATH
        ), shell=True)
