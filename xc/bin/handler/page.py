# coding: utf-8
from zbase.web import core
from zbase.web import template

import logging

log = logging.getLogger()



class Root(core.Handler):
    def GET(self):
        self.write(template.render('index.html'))
