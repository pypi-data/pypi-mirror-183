import time
from machine import Pin, PWM


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
        """
        A button is a simple input that can be pressed.
        :param pin: pin
        :param default: default value
        """
        super().__init__(pin, default)
        self.default = default

    def is_pressed(self):
        """
        Returns True if the button is pressed.
        """
        if self.pin.value() != self.default:
            time.sleep_ms(15)
            if self.pin.value() != self.default:
                return True
        return False


class Led:

    def __init__(self, pin, status=False, grade=0xFFFF):
        """
        :param pin: pin
        :param grade: 0-65535
        """
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(1000)
        self.grade = grade
        self.pwm.duty_u16(grade if status else 0)

    def switch(self, grade=None):
        """
        Switches the LED on or off.
        :param grade: 0-65535
        """
        if grade:
            self.grade = grade
            self.pwm.duty_u16(self.grade)
        elif self.pwm.duty_u16() == 0:
            self.pwm.duty_u16(self.grade)
        else:
            self.pwm.duty_u16(0)

    def on(self):
        self.pwm.duty_u16(self.grade)

    def off(self):
        self.pwm.duty_u16(0)

    def read(self):
        return self.pwm.duty_u16()

    def write(self, value):
        self.pwm.duty_u16(value)
