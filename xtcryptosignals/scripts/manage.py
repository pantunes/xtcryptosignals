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
@click.option(
    '--start',
    is_flag=True,
    help="Start xt-server, xt-client and xt-ticker",
)
@click.option(
    '--stop',
    is_flag=True,
    help="Stop xt-server, xt-client and xt-ticker",
)
@click.option(
    '--restart',
    is_flag=True,
    help="Restart xt-server, xt-client and xt-ticker",
)
def main(start, stop, restart):
    if start:
        subprocess.call("sh {}/xt-start.sh".format(SCRIPT_PATH), shell=True)
    elif stop:
        subprocess.call("sh {}/xt-stop.sh".format(SCRIPT_PATH), shell=True)
    elif restart:
        subprocess.call("sh {}/xt-stop.sh ; sh {}/xt-start.sh".format(
            SCRIPT_PATH, SCRIPT_PATH
        ), shell=True)
    else:
        click.echo('Nothing to do!')
