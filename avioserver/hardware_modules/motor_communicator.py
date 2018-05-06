# -*- coding: utf-8 -*-
import Adafruit_PCA9685


class MotorController(object):
    pwm = None
    aerlon_channel = 0
    aerlon_opposite_channel = 1

    # Configure min and max servo pulse lengths
    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096

    aerlon_max = 3000

    def __init__(self):
        try:
            self.pwm = Adafruit_PCA9685.PCA9685()
            self.pwm.set_pwm_freq(60)
        except RuntimeError:
            self.pwm = None

    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000  # 1,000,000 us per second

        pulse_length //= 60  # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096  # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        if self.pwm:
            self.pwm.set_pwm(channel, 0, pulse)

    def set_aerlon(self, position):
        if self.pwm:
            self.pwm.set_pwm(self.aerlon_channel, 0, position)
            self.pwm.set_pwm(self.aerlon_opposite_channel, 0, self.aerlon_max - position)

