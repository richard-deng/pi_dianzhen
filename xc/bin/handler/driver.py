# coding: utf-8
import time
import datetime
import RPi.GPIO as gpio

A1 = 11
A2 = 12
B1 = 13
B2 = 15
C1 = 16
C2 = 18
D1 = 29
D2 = 31

HW = 22
FM = 7

arr = [A1, A2, B1, B2, C1, C2, D1, D2]


def init_hw():
    gpio.setup(HW, gpio.IN)


def init_fm():
    gpio.setup(FM, gpio.OUT)
    gpio.output(FM, gpio.HIGH)


def enable_fm():
    gpio.output(FM, gpio.LOW)


def reset_fm():
    gpio.output(FM, gpio.HIGH)


def init_board():
    gpio.setmode(gpio.BOARD)


def out_put():
    for pin in arr:
        gpio.setup(pin, gpio.OUT)


def reset():
    for pin in arr:
        gpio.output(pin, gpio.HIGH)


def read_hw():
    v = gpio.input(HW)
    return v

def motor_a():
    gpio.output(A1, gpio.HIGH)
    gpio.output(A2, gpio.LOW)


def motor_reverse_a():
    gpio.output(A1, gpio.LOW)
    gpio.output(A2, gpio.HIGH)


def motor_b():
    gpio.output(B1, gpio.HIGH)
    gpio.output(B2, gpio.LOW)


def motor_reverse_b():
    gpio.output(B1, gpio.LOW)
    gpio.output(B2, gpio.HIGH)


def motor_c():
    gpio.output(C1, gpio.LOW)
    gpio.output(C2, gpio.HIGH)


def motor_reverse_c():
    gpio.output(C1, gpio.HIGH)
    gpio.output(C2, gpio.LOW)


def motor_d():
    gpio.output(D1, gpio.LOW)
    gpio.output(D2, gpio.HIGH)


def motor_reverse_d():
    gpio.output(D1, gpio.HIGH)
    gpio.output(D2, gpio.LOW)


def finish():
    gpio.cleanup()


def qianjin():
    try:
        reset()
        motor_a()
        motor_b()
        motor_c()
        motor_d()
    except Exception as e:
        print str(e)
        finish()


def reverse():
    try:
        reset()
        motor_reverse_a()
        motor_reverse_b()
        motor_reverse_c()
        motor_reverse_d()
    except Exception as e:
        print str(e)
        finish()


def left():
    try:
        reset()
        motor_a()
        motor_c()
    except Exception as e:
        print str(e)
        finish()


def right():
    try:
        reset()
        motor_b()
        motor_d()
    except Exception as e:
        print str(e)
        finish()


def run():
    init_board()
    out_put()
    reset()
    qianjin()
    time.sleep(3)
    finish()

if __name__ == '__main__':
    run()
