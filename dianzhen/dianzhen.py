# coding: utf-8
import time
import RPi.GPIO as GPIO
# TIMEOUT
timeout = 3

# HIGH
channel_12 = 12
channel_16 = 16
channel_high_list = [12, 16]
# HIGH END

# LOW
channel_7 = 7
channel_13 = 13
channel_15 = 15
channel_29 = 29
channel_31 = 31
channel_33 = 33
channel_36 = 36
channel_37 = 37
channel_low_list = [7, 13, 15, 29, 31, 33, 36, 37]
# LOW_END

# OUT
out_list = channel_high_list + channel_low_list
# OUT_END

# COL
col_list = [37, 36, 13, 33, 15, 31, 29, 7]
# COL END

def init_output():
    for channel in out_list:
        GPIO.setup(channel, GPIO.OUT)

def set_high():
    for channel in channel_high_list:
        GPIO.output(channel_high_list, GPIO.HIGH)

def set_high_low():
    for channel in channel_high_list:
        GPIO.output(channel_high_list, GPIO.LOW)

def set_low():
    for channel in channel_low_list:
        GPIO.output(channel, GPIO.LOW)

def set_low_high():
    for channel in channel_low_list:
        GPIO.output(channel, GPIO.HIGH)

def set_board():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)


def donghua_one():
    try:
        set_board()
        init_output()
        while True:
            set_high()
            time.sleep(1)
            set_high_low()
            time.sleep(1)
    except Exception:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()


def donghua_two():
    print 'run donghua two'
    try:
        set_board()
        init_output()
        for channel in col_list:
            print 'channel ', channel
            GPIO.output(channel, GPIO.LOW)
            time.sleep(1)
            GPIO.output(channel, GPIO.HIGH)
            time.sleep(1)
    except Exception:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()


def run():
    donghua_two()

if __name__ == '__main__':
    run()
