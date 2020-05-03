__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import requests
import wikipediaapi
from bs4 import BeautifulSoup
from datetime import date
from celery.task import task
from celery.exceptions import Ignore
from celery import states
from xtcryptosignals.common.utils import use_mongodb
from xtcryptosignals.server.api.projects.models import Project
from xtcryptosignals.tasks.models.project_twitter import ProjectTwitter
from xtcryptosignals.tasks import settings as s


def _get_twitter_num_followers(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    try:
        return int(
            soup.find(href=f"/{url.rsplit('/', 1)[-1]}/followers").find(
                attrs={"class": "ProfileNav-value"}
            )["data-count"]
        )
    except AttributeError:
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

    try:
        for p in Project.objects:
            if p["wikipedia"]:
                p.summary = _get_wikipedia_summary(p["wikipedia"])
            p.save()
            if p["twitter"]:
                ProjectTwitter(
                    project=p,
                    num_followers=_get_twitter_num_followers(p["twitter"]),
                    added_on=date.today(),
                ).save()
    except Exception as error:
        logger.error("twitter error: {}".format(str(error)))
        self.update_state(state=states.FAILURE, meta=str(error))
        raise Ignore()
