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


def set_board():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)


def run():
    try:
        while True:
            set_high()
            time.sleep(3)
            set_high_low()
            time.sleep(3)
    except Exception:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    set_board()
    init_output()
    set_low()
    run()
