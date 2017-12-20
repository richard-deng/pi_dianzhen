# coding: utf-8
import time
import RPi.GPIO as gpio

pin_31 = 31
pin_33 = 33
pin_35 = 35
pin_37 = 37
CLOCKWISE = 1
COUNTER_CLOCKWISE = 2
pins = [pin_31, pin_33, pin_35, pin_37]

def init_board():
    gpio.setmode(gpio.BOARD)


def set_output():
    gpio.setup(pin_31, gpio.OUT)
    gpio.setup(pin_33, gpio.OUT)
    gpio.setup(pin_35, gpio.OUT)
    gpio.setup(pin_37, gpio.OUT)


def out_high(pin):
    gpio.output(pin, gpio.HIGH)


def out_low(pin):
    gpio.output(pin, gpio.LOW)

def read():
    v1 = gpio.input(pin_31)
    v2 = gpio.input(pin_33)
    v3 = gpio.input(pin_35)
    v4 = gpio.input(pin_37)
    print v1, v2, v3, v4


def finish():
    gpio.cleanup()


def rotate(direction):
    for i in range(0, 4):
        if CLOCKWISE == direction:
            for j in range(0, 4):
                if j == i:
                    out_high(pins[j])
                else:
                    out_low(pins[j])
                read()
        else:
            for i in range(0, 4):
                if  j == i:
                    out_high(pins[j])
                else:
                    out_low(pins[j])
                read()
    time.sleep(1)


def run():
    try:
        init_board()
        set_output()
        time.sleep(1)
        for i in range(0, 501):
            rotate(CLOCKWISE)

    except Exception:
        finish()
    finally:
        finish()

if __name__ == '__main__':
    run()
