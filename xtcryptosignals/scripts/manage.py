__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
import click
import subprocess
from shutil import copyfile


SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))


@click.command(
    context_settings=dict(help_option_names=['-h', '--help'])
)
@click.argument(
    'operation', required=True, type=click.Choice(
        ('copy-config-files', 'start', 'stop', 'restart',)
    )
)
def main(operation):
    if operation == 'copy-config-files':
        for x in (
                'client.prod.env',
                'server.prod.env',
                'client.dev.env',
                'server.dev.env'
        ):
            filepath_source = os.path.join(SCRIPT_PATH, '../config', x)
            filepath_dest = os.path.join(os.getcwd(), 'config', x)
            try:
                copyfile(filepath_source, filepath_dest)
                click.echo(
                    'Copied from {} to {}'.format(
                        filepath_source, filepath_dest
                    )
                )
            except IOError:
                os.makedirs(os.path.dirname(filepath_dest))
                click.echo('Created folder {}'.format(filepath_dest))
                copyfile(filepath_source, filepath_dest)
                click.echo(
                    'Copied from {} to {}'.format(
                        filepath_source, filepath_dest
                    )
                )
        return
    if operation == 'start':
        subprocess.call("sh {}/xt-start.sh".format(SCRIPT_PATH), shell=True)
        return
    if operation == 'stop':
        subprocess.call("sh {}/xt-stop.sh".format(SCRIPT_PATH), shell=True)
        return
    subprocess.call("sh {}/xt-stop.sh ; sh {}/xt-start.sh".format(
        SCRIPT_PATH, SCRIPT_PATH
    ), shell=True)
