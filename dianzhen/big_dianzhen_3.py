#coding: utf-8
import time
import RPi.GPIO as gpio
channel_12_h = 12
channel_16_h = 16
channel_18_h = 18
channel_22_h = 22
channel_32_h = 32
channel_36_h = 36
channel_38_h = 38
channel_40_h = 40

channel_7_l = 7
channel_11_l = 11
channel_13_l = 13
channel_15_l = 15
channel_29_l = 29
channel_31_l = 31
channel_33_l = 33
channel_35_l = 35


row = [
    channel_12_h, channel_16_h, channel_18_h, channel_22_h,
    channel_32_h, channel_36_h, channel_38_h, channel_40_h,
]
col = [
    channel_7_l, channel_11_l, channel_13_l, channel_15_l,
    channel_29_l, channel_31_l, channel_33_l, channel_35_l,
]
row_map = {
    1: channel_12_h,
    2: channel_16_h,
    3: channel_18_h,
    4: channel_22_h,
    5: channel_32_h,
    6: channel_36_h,
    7: channel_38_h,
    8: channel_40_h
}
col_map = {
    1: channel_7_l,
    2: channel_11_l,
    3: channel_13_l,
    4: channel_15_l,
    5: channel_29_l,
    6: channel_31_l,
    7: channel_33_l,
    8: channel_35_l,
}


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
    八行八列全亮
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


def on_row_col(row, col):
    row = row_map.get(row)
    col = col_map.get(col)
    gpio.output(row, gpio.HIGH)
    gpio.output(col, gpio.LOW)


def off_row_col(row, col):
    row = row_map.get(row)
    col = col_map.get(col)
    gpio.output(row, gpio.LOW)


def chose_row_col(row, col):
    row = row_map.get(row)
    col = col_map.get(col)
    gpio.setup(row, gpio.OUT)
    gpio.setup(col, gpio.OUT)


def init_board():
    gpio.setmode(gpio.BOARD)
    # gpio.setwarnings(gpio.False)


def finish():
    gpio.cleanup()


def eg_row_col():
    init_board()
    chose_row_col(8, 8)
    on_row_col(8, 8)
    time.sleep(5)
    off_row_col(8, 8)
    time.sleep(1)
    finish()


def dong_hua_liushui():
    try:
        while True:
            for row in range(1, 9):
                for col in range(1, 9):
                    print row, col
                    init_board()
                    chose_row_col(row, col)
                    on_row_col(row, col)
                    time.sleep(0.1)
                    finish()
            print 'next cycle'
    except Exception as e:
        finish()
    finally:
        finish()


def echo_0():
   init_board()
   gpio.setup(row_map[2], gpio.OUT)    
   gpio.output(row_map[2], gpio.HIGH)    
   gpio.setup(col_map[4], gpio.OUT)    
   gpio.output(col_map[4], gpio.LOW)
   gpio.setup(col_map[5], gpio.OUT)    
   gpio.output(col_map[5], gpio.LOW)
   gpio.setup([row_map[3], row_map[4], row_map[5], row_map[6]], gpio.OUT)    
   gpio.output([row_map[3], row_map[4], row_map[5], row_map[6]], gpio.HIGH)
   gpio.setup([col_map[3], col_map[6]], gpio.OUT)
   gpio.output([col_map[3], col_map[6]], gpio.LOW)
   time.sleep(5)
   finish()


def run():
    # row_1_col_1()
    # row_4_col_8()
    # eg_row_col()
    dong_hua_liushui()
    # echo_0()

if __name__ == '__main__':
    run()
