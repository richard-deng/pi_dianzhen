# coding: utf-8
from driver import *
from zbase.web import core

class Ping(core.Handler):
    def GET(self):
        self.write('OK')


class QianJin(core.Handler):
    def GET(self):
        print 'qianjin'
        qianjin()
        self.write('OK')


class Reverse(core.Handler):
    def GET(self):
        print 'reverse'
        reverse()
        self.write('OK')


class Left(core.Handler):
    def GET(self):
        print 'left'
        left()
        self.write('OK')


class Right(core.Handler):
    def GET(self):
        print 'right'
        right()
        self.write('OK')


class Stop(core.Handler):
    def GET(self):
        print 'stop'
        reset()
        finish()
        self.write('OK')


class Start(core.Handler):
    def GET(self):
        print 'prepare'
        init_board()
        out_put()
        self.write('OK')
