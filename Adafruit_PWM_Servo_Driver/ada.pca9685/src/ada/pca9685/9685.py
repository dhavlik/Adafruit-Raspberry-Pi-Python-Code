#coding:utf8

import i2c
import math
import time

DEFAULT = []

SUBADR1 = 0x02
SUBADR2 = 0x03
SUBADR3 = 0x04
MODE1 = 0x00
PRESCALE = 0xFE
LED0_ON_L = 0x06
LED0_ON_H = 0x07
LED0_OFF_L = 0x08
LED0_OFF_H = 0x09
ALLLED_ON_L = 0xFA
ALLLED_ON_H = 0xFB
ALLLED_OFF_L = 0xFC
ALLLED_OFF_H = 0xFD


class PWM(object):
    """API for interfacing an PCA9685."""

    i2c = None

    def __init__(self, address=0x40, bus=DEFAULT, debug=False):
        params = dict(address=address, bus=bus)
        if bus == DEFAULT:
            # Urks: Use default bus specified in Adafruit_I2C.__init__
            # signature.
            # Better refactor the I2C class to take only port number.
            del params['bus']
        self.i2c = i2c.Adafruit_I2C(**params)
        self.address = address
        self.debug = debug
        if (self.debug):
            print "Reseting PCA9685"
        self.i2c.write8(MODE1, 0x00)

    def setPWMFreq(self, freq):
        """Sets the PWM frequency."""
        prescaleval = 25000000.0    # 25MHz
        prescaleval /= 4096.0       # 12-bit
        prescaleval /= float(freq)
        prescaleval -= 1.0
        if (self.debug):
            print "Setting PWM frequency to %d Hz" % freq
            print "Estimated pre-scale: %d" % prescaleval
        prescale = math.floor(prescaleval + 0.5)
        if (self.debug):
            print "Final pre-scale: %d" % prescale
        oldmode = self.i2c.readU8(MODE1)
        newmode = (oldmode & 0x7F) | 0x10             # sleep
        self.i2c.write8(MODE1, newmode)        # go to sleep
        self.i2c.write8(PRESCALE, int(math.floor(prescale)))
        self.i2c.write8(MODE1, oldmode)
        time.sleep(0.005)
        self.i2c.write8(MODE1, oldmode | 0x80)

    def setPWM(self, channel, on, off):
        """Sets a single PWM channel."""
        self.i2c.write8(LED0_ON_L + 4 * channel, on & 0xFF)
        self.i2c.write8(LED0_ON_H + 4 * channel, on >> 8)
        self.i2c.write8(LED0_OFF_L + 4 * channel, off & 0xFF)
        self.i2c.write8(LED0_OFF_H + 4 * channel, off >> 8)
