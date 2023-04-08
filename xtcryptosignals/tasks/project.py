__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from datetime import date

import requests
import wikipediaapi
from celery import states
from celery.exceptions import Ignore
from celery.task import task

from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.server.api.projects.models import Project
from xtcryptosignals.tasks import settings as s
from xtcryptosignals.tasks.models.project_twitter import ProjectTwitter


def _get_twitter_num_followers(url):
    headers = {"Authorization": f"Bearer {s.TWITTER_BEARER}"}

    _url = f"https://api.twitter.com/2/users/by/username/{url.rsplit('/', 1)[-1]}?user.fields=public_metrics"

    response = requests.get(_url, headers=headers)
    if response.status_code != 200:
        return

    try:
        return response.json()["data"]["public_metrics"]["followers_count"]
    except KeyError:
        return


def _get_wikipedia_summary(url):
    wiki_wiki = wikipediaapi.Wikipedia("en")
    page_py = wiki_wiki.page(url.rsplit("/", 1)[-1])
    p = page_py.summary[0:1000]
    return p[: p.rfind(". ") + 1]


@task(bind=True)
@use_mongodb(db=s.MONGODB_NAME, host=s.MONGODB_HOST, port=s.MONGODB_PORT)
def update(self):
    logger = self.get_logger()
    today = date.today()
    try:
        for p in Project.objects:

            if p.wikipedia:
                p.summary = _get_wikipedia_summary(p.wikipedia)
                p.save()

            if p.twitter:
                pt = ProjectTwitter(
                    project=p,
                    num_followers=_get_twitter_num_followers(p.twitter),
                    added_on=today,
                )
                pt.save()

    except Exception as error:
        logger.error(f"twitter error: {error}")
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
