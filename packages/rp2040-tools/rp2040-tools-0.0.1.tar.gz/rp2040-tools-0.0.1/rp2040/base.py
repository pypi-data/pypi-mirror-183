import time
from machine import Pin


class SimpleOut:

    def __init__(self, pin, default=0):
        self.pin = Pin(pin, Pin.OUT)
        self.pin.value(default)

    def read(self):
        return self.pin.value()

    def write(self, value):
        return self.pin.value(value)


class SimpleIn:

    def __init__(self, pin, default=Pin.PULL_UP):
        self.pin = Pin(pin, Pin.IN, default)

    def read(self):
        return self.pin.value()

    def write(self, value):
        return self.pin.value(value)


class Button(SimpleIn):

    def __init__(self, pin, default=Pin.PULL_UP):
        super().__init__(pin, default)
        self.default = default

    def is_pressed(self):
        if self.pin.value() != self.default:
            time.sleep_ms(15)
            if self.pin.value() != self.default:
                return True
        return False


class Led(SimpleOut):

    def __init__(self, pin, default=0):
        super().__init__(pin, default)

    def switch(self):
        self.pin.value(not self.pin.value())

    def on(self):
        self.pin.value(1)

    def off(self):
        self.pin.value(0)

