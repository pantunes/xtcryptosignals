__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import click
from xtcryptosignals.tasks import settings as s
from xtcryptosignals.tasks import ticker


@click.command(
    context_settings=dict(help_option_names=['-h', '--help'])
)
@click.option(
    '--test',
    is_flag=True,
    help="Process 1 iteration for all configured "
         "coins and/or tokens."
         "(Useful for testing purposes)",
)
@click.option(
    '--list-config',
    type=click.Choice(['exchanges', 'currencies']),
    help="List 'exchanges' or 'currencies' (coins or tokens) per exchange "
         "that the tool currently supports."
)
@click.option(
    '--enable-messaging',
    is_flag=True,
    help="Enable real-time crypto data message broadcasting."
)
@click.option(
    '--log-minimal',
    is_flag=True,
    help="Only log errors and important warnings in stdout."
)
@click.option(
    '--version',
    is_flag=True,
    help="Show version."
)
@click.pass_context
def main(ctx, test, list_config, enable_messaging, log_minimal, version):
    """
    Use this tool to collect and broadcast data from configured coins
    or/and tokens from configured crypto-currencies exchanges.
    """
    if list_config:
        if list_config == 'currencies':
            import pprint
            click.echo(pprint.pprint(s.SYMBOLS_PER_EXCHANGE))
        elif list_config == 'exchanges':
            click.echo('\n'.join(s.EXCHANGES))
        ctx.exit()

    beat_kwargs = dict(
        enable_messaging=enable_messaging,
        log_minimal=log_minimal,
    )

    if test:
        ticker.test(**beat_kwargs)
        ctx.exit()

    if version:
        from xtcryptosignals import __title__, __version__
        click.echo('{} {}'.format(__title__, __version__))
        ctx.exit()

    from celery import current_app
    from celery.bin import worker

    app = current_app._get_current_object()

    app.config_from_object('xtcryptosignals.tasks.celeryconfig')

    # updates beat config dynamically
    app.conf.beat_schedule['ticker'].update(kwargs=beat_kwargs)

    worker = worker.worker(app=app)
    worker.run(beat=True, loglevel=ticker.logging.INFO)
