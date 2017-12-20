import time
import traceback
import datetime
import RPi.GPIO as gpio

pin_f = 7
pin_g = 12
last_time = None

def init_board():
    gpio.setmode(gpio.BOARD)


def init_f():
    gpio.setup(pin_f, gpio.OUT)


def init_g():
    gpio.setup(pin_g, gpio.IN)


def enable_f():
    now = datetime.datetime.now()
    print 'enable_f now', now
    print 'enable_f last_time', last_time
    gpio.output(pin_f, gpio.LOW)
    time.sleep(0.3)
    disable_f()


def disable_f():
    gpio.output(pin_f, gpio.HIGH)


def read_g():
    global last_time
    now = datetime.datetime.now()
    v = gpio.input(pin_g)
    print 'v', v,  now
    if v == 1:
        print 'last_time', last_time
        if last_time == None:
            last_time = now
        elif now.second - last_time.second > 0 and now.second - last_time.second <= 1:
            enable_f()
            last_time = now
        else:
            last_time = None
            disable_f()
    else:
        disable_f()

def finish():
    gpio.cleanup()

def run():
    try:
        init_board()
        init_f()
        init_g()
        while True:
            read_g()
    except Exception as e:
        print traceback.format_exc()
        finish()
    finally:
        finish()

run()
