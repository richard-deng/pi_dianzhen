import RPi.GPIO as gpio
rs = 12
en = 18
d0 = 11
d1 = 13
d2 = 15
d3 = 29

d4 = 31
d5 = 33
d6 = 35
d7 = 37

out = [rs, en, d0, d1, d2, d3, d4, d5, d6, d7]
# address  0x00 0x3F
def init_out():
    for pin in out:
        gpio.setup(pin, gpio.OUT)


def init_board():
    gpio.setmode(gpio.BOARD)


def finish():
    gpio.cleanup()


def en_low():
    gpio.output(en, gpio.LOW)

def en_high():
    gpio.output(en, gpio.HIGH)

def write_command(command):
    gpio.output(en, gpio.HIGH)
    gpio.output(rs, gpio.LOW)
    # write command
    time.sleep(0.5)
    gpio.output(en, gpio.LOW)

def write_content(data):
    gpio.output(en, gpio.HIGH)
    gpio.output(rs, gpio.HIGH)
    # write data
    time.sleep(0.5)
    gpio.output(en, gpio.LOW)

def run():
    try:
        pass
    except Exception:
        finish()
    finally:
        finish()



if __name__ == '__main__':
    run()



