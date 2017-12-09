#coding: utf-8
import time
import RPi.GPIO as gpio
channel_12_h = 12
channel_16_h = 16
channel_18_h = 18
channel_22_h = 22
channel_32_h = 32

channel_7_l = 7
channel_13_l = 13
channel_15_l = 15
channel_29_l = 29
channel_31_l = 31
channel_33_l = 33
channel_37_l = 37
channel_36_l = 36

row = [channel_12_h, channel_16_h, channel_18_h, channel_22_h, channel_32_h]
col = [channel_7_l, channel_13_l, channel_15_l, channel_29_l, channel_31_l, channel_33_l, channel_37_l, channel_36_l]


def row_1_col_1():
    """
    第一行第一列闪亮
    """
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


def row_4_col_8():
    """
    前五行和八列同时点亮
    """
    try:
        while True:
            gpio.setmode(gpio.BOARD)
            for channel in row:
                gpio.setup(channel, gpio.OUT)
                gpio.output(channel, gpio.HIGH)
            for channel in col:
                gpio.setup(channel, gpio.OUT)
                gpio.output(channel, gpio.LOW)
            time.sleep(3)
            gpio.cleanup()
            time.sleep(3)
    except Exception:
        gpio.cleanup()
    finally:
        gpio.cleanup()


def run():
    # row_1_col_1()
    row_4_col_8()


if __name__ == '__main__':
    run()

