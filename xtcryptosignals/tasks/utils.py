__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from importlib import import_module


def get_class(folder, module):
    exchange_module = import_module(f"{folder}.{module}")
    module_class_name = "".join([x.capitalize() for x in module.split("_")])
    return getattr(exchange_module, module_class_name)


def convert_to_seconds(x):
    _t = x[-1]
    try:
        seconds = int(x[:-1])
    except ValueError:
        raise ValueError(f"Invalid item: {x}")
    if _t == "s":
        return seconds
    minutes = seconds * 60
    if _t == "m":
        return minutes
    hours = minutes * 60
    if _t == "h":
        return hours
    days = hours * 24
    if _t == "d":
        return days
    weeks = days * 7
    if _t == "w":
        return weeks
    months = weeks * 4
    year = months * 12
    if _t == "y":
        return year
    raise ValueError(f"Undefined item: {x}")


def terminate_running_jobs(logger, jobs):
    logger.warning(f"Number of jobs completed: {len(jobs)}")
    for j in jobs:
        if j["job"].is_alive():
            logger.warning(
                f"Exceeded timeout of {j['timeout']} seconds in {j['job'].name}"
            )
            j["job"].terminate()
            j["job"].join()
