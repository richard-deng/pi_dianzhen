import RPi.GPIO as gpio

pin_rs = 12
pin_en = 18

pin_d0 = 11
pin_d1 = 13
pin_d2 = 15
pin_d3 = 29
pin_d4 = 31
pin_d5 = 33
pin_d6 = 35
pin_d7 = 37

def write_command():
    gpio.setup(pin_rs, gpio.OUT)
    gpio.output(pin_rs, gpio.LOW)


def write_data():
    gpio.setup(pin_rs, gpio.OUT)
    gpio.output(pin_rs, gpio.HIGH)




