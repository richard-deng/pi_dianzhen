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

HP = 7

arr = [A1, A2, B1, B2, C1, C2, D1, D2]

def init_board():
    gpio.setmode(gpio.BOARD)


def out_put():
    for pin in arr:
        gpio.setup(pin, gpio.OUT)

def reset():
    for pin in arr:
        gpio.output(pin, gpio.HIGH)

def in_set():
    gpio.setup(HP, gpio.IN)


def read_hp():
    v = gpio.input(HP)
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
        motor_a()
        motor_b()
        motor_c()
        motor_d()
    except Exception as e:
        print str(e)
        finish()


def reverse():
    try:
        motor_reverse_a()
        motor_reverse_b()
        motor_reverse_c()
        motor_reverse_d()
    except Exception as e:
        print str(e)
        finish()


def left():
    try:
        motor_a()
        motor_c()
    except Exception as e:
        print str(e)
        finish()


def right():
    try:
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
