__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import click
from xtcryptosignals.tasks import ticker
from xtcryptosignals.tasks import settings as s


def _prepare_celery_beat(app, *_, tasks, **kwargs):
    # enable single tasks
    for k in app.conf.beat_schedule.copy():
        if k not in tasks:
            del app.conf.beat_schedule[k]

    # updates beat config dynamically
    if "ticker" in app.conf.beat_schedule:
        from xtcryptosignals.tasks.caching import prepare_cache

        # pre-cache all needed data
        prepare_cache()

        app.conf.beat_schedule["ticker"].update(kwargs=kwargs["beat_kwargs"])


def _prepare_queue(app, tasks, queue):
    app.conf.task_routes = {}
    for t in tasks:
        app.conf.task_routes.update(
            {f"xtcryptosignals.tasks.{t}.update": {"queue": queue}}
        )


_list_of_tasks = [
    "cfgi",
    "project",
    "tether",
    "ticker",
    "notifications",
    "order_book",
]


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--test",
    is_flag=True,
    help="Process 1 iteration for all configured "
    "coins and/or tokens. (Useful for testing purposes)",
)
@click.option(
    "--list-config",
    type=click.Choice(["exchanges", "currencies"]),
    help="List 'exchanges' or 'currencies' (coins or tokens) per exchange "
    "that are currently supported.",
)
@click.option(
    "-t",
    "--task",
    type=click.Choice(_list_of_tasks, case_sensitive=False),
    default=_list_of_tasks,
    multiple=True,
    help="Task to be executed. If this parameter is omitted all "
    "tasks will be started",
)
@click.option(
    "-q",
    "--queue",
    type=str,
    default="celery",
    help="Queue name to execute indicated tasks.",
)
@click.option(
    "--disable-ticker-messaging",
    is_flag=True,
    default=False,
    help="Disable ticker message broadcasting.",
)
@click.option(
    "--log-ticker-minimal",
    is_flag=True,
    default=False,
    help="Only log ticker errors and important warnings in stdout.",
)
@click.option("--version", is_flag=True, help="Show version.")
@click.pass_context
def main(
    ctx,
    test,
    list_config,
    disable_ticker_messaging,
    log_ticker_minimal,
    task,
    queue,
    version,
):
    """
    Use this tool to start all or part of the tasks.
    """
    if list_config:
        if list_config == "currencies":
            import pprint

            click.echo(pprint.pprint(s.SYMBOLS_PER_EXCHANGE))
        elif list_config == "exchanges":
            click.echo("\n".join(s.EXCHANGES))
        ctx.exit()

    beat_kwargs = dict(
        disable_ticker_messaging=disable_ticker_messaging,
        log_ticker_minimal=log_ticker_minimal,
    )

    if test:
        ticker.test(**beat_kwargs)
        ctx.exit()

    if version:
        from xtcryptosignals import __title__, __version__

        click.echo("{} {}".format(__title__, __version__))
        ctx.exit()

    from celery import current_app
    from celery.bin import worker

    app = current_app._get_current_object()

    app.config_from_object("xtcryptosignals.tasks.celeryconfig")

    # tasks passed by argument or default
    tasks = list(task)

    _prepare_celery_beat(app, tasks=tasks, beat_kwargs=beat_kwargs)
    _prepare_queue(app, tasks=tasks, queue=queue)

    worker = worker.worker(app=app)
    worker.run(
        beat=True,
        queues=[queue],
        schedule_filename=f"celerybeat-schedule-{queue}.db",
        loglevel=ticker.logging.INFO,
    )
