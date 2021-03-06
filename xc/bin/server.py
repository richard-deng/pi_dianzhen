# -*- coding: utf-8 -*-
import os
import sys
HOME = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(os.path.dirname(HOME), 'conf'))

from zbase.base import logger
# from zbase.base import dbpool
from zbase.web import core
from zbase.web import runner
from zbase.web import template

import config
import urls

if config.LOGFILE:
    log = logger.install(config.LOGFILE, when='MIDNIGHT')
else:
    log = logger.install('stdout')

template.install(config.template)

config.URLS = urls.urls


def install_db():
    dbpool.install(config.database)

log.info('<<< server start >>>')
# install_db()
app = core.WebApplication(config)


if __name__ == '__main__':
    runner.run_simple(app, host=config.HOST, port=config.PORT)
