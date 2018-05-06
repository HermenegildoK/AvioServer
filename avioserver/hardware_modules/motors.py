# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

pwm = Adafruit_PCA9685.PCA9685()
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# servo motors and channels

aerlon_channel_1 = 0
aerlon_channel_2 = 1 //always opposite

elevator_channel = 2 // motor benc

gas_channel = 3

kormilo_channel = 4

flaps_channel = 5

parachute_channel = 6; 

aerlon_channel_1_min = 150; //for trimming
aerlon_channel_1_max = 500; //for trimming
aerlon_channel_1_zero = 300; //for trimming

aerlon_channel_2_min = 150; //for trimming
aerlon_channel_2_max = 500; //for trimming
aerlon_channel_2_zero = 300;

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
    
def _map(value,istart,istop,ostart,ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop-istart))

#zero is 127
def set_aerlon(position):
    pwm.set_pwm(aerlon_channel_1,0, _map(position,0,255,aerlon_channel_1_min,aerlon_channel_1_max))
    pwm.set_pwm(aerlon_channel_1,0, _map(position,255,0,aerlon_channel_1_min,aerlon_channel_1_max))
	
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
#set_aerlon(0)
#set_aerlon(0)
time.sleep(1)
pwm.set_pwm(1,0,50) #to zero
pwm.set_pwm(0,0,50) #to zero
print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    #set_aerlon(500)
    pwm.set_pwm(1,0,aerlon_channel_1_min)
    time.sleep(1)
    pwm.set_pwm(1,0,aerlon_channel_1_max)
    time.sleep(1)
