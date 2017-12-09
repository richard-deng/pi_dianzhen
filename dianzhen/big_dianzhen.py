#coding: utf-8
import time
import RPi.GPIO as gpio
channel_12_h = 12
channel_7_l = 7

def run():
    try:
        gpio.setmode(gpio.BOARD)
        gpio.setup(channel_12_h, gpio.OUT)
        gpio.setup(channel_7_l, gpio.OUT)
        gpio.output(channel_7_l, gpio.LOW)
        while True:
            gpio.output(channel_7_l, gpio.HIGH)
            time.sleep(1)
            gpio.output(channel_7_l, gpio.LOW)
            time.sleep(1)
    except Exception:
        gpio.cleanup()
    finally:
        gpio.cleanup()


if __name__ == '__main__':
    run()

