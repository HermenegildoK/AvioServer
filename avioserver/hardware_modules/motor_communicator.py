# -*- coding: utf-8 -*-
import Adafruit_PCA9685


class MotorController(object):
    pwm = None

    aerlon_channel_1 = 0
    aerlon_channel_2 = 1 #always opposite

    elevator_channel = 2 # motor benc

    gas_channel = 3

    kormilo_channel = 4

    flaps_channel = 5

    parachute_channel = 6

    aerlon_channel_1_min = 150 #for trimming
    aerlon_channel_1_max = 500 #for trimming
    aerlon_channel_1_zero = 300 #for trimming

    aerlon_channel_2_min = 150 #for trimming
    aerlon_channel_2_max = 500 #for trimming
    aerlon_channel_2_zero = 300

    def __init__(self):
        try:
            self.pwm = Adafruit_PCA9685.PCA9685()
            self.pwm.set_pwm_freq(60)
            self.pwm.set_pwm(1,0,50) #to zero
            self.pwm.set_pwm(0,0,50) #to zero
        except RuntimeError as err:
            print(err)
            self.pwm = None
            
        
    def _map(self, value, istart, istop, ostart, ostop):
        return int(ostart + (ostop - ostart) * ((value - istart) / (istop-istart)))

    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096     # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        
        if self.pwm:
            self.pwm.set_pwm(channel, 0, pulse)

    def set_aerlon(self, position):
        if self.pwm:
            print(position)
            self.pwm.set_pwm(
                self.aerlon_channel_1,
                0,
                position
            )
            self.pwm.set_pwm(
                self.aerlon_channel_2,
                0,
                self.aerlon_channel_2_max-position
            )

