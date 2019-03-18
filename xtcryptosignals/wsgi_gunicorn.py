__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import multiprocessing
import gunicorn.app.base


NUMBER_OF_WORKERS = (multiprocessing.cpu_count() * 2) + 1


class WSGIGunicorn(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(WSGIGunicorn, self).__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def start(handler, host, port, workers=None):
    options = {
        'bind': '%s:%s' % (host, port),
        'workers': workers or NUMBER_OF_WORKERS,
    }

    WSGIGunicorn(handler, options).run()
