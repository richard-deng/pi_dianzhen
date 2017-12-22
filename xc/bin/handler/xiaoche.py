# coding: utf-8
from driver import *
from zbase.web import core

class Ping(core.Handler):
    def GET(self):
        self.write('OK')


class QianJin(core.Handler):
    def GET(self):
        self.set_headers({'Content-Type': 'application/json; charset=UTF-8'})
        print 'qianjin'
        qianjin()
        return self.write('OK')


class Reverse(core.Handler):
    def GET(self):
        self.set_headers({'Content-Type': 'application/json; charset=UTF-8'})
        print 'reverse'
        reverse()
        return self.write('OK')


class Left(core.Handler):
    def GET(self):
        self.set_headers({'Content-Type': 'application/json; charset=UTF-8'})
        print 'left'
        left()
        return self.write('OK')


class Right(core.Handler):
    def GET(self):
        self.set_headers({'Content-Type': 'application/json; charset=UTF-8'})
        print 'right'
        right()
        return self.write('OK')


class Stop(core.Handler):
    def GET(self):
        self.set_headers({'Content-Type': 'application/json; charset=UTF-8'})
        print 'stop'
        reset()
        finish()
        return self.write('OK')


class Start(core.Handler):
    def GET(self):
        self.set_headers({'Content-Type': 'application/json; charset=UTF-8'})
        print 'prepare'
        init_board()
        out_put()
        return self.write('OK')
