# coding: utf-8
from zbase.web import core
from zbase.web import template

import logging

log = logging.getLogger()


class Pc(core.Handler):
    def GET(self):
        self.write(template.render('pc.html'))


class Wap(core.Handler):
    def GET(self):
        self.write(template.render('wap.html'))