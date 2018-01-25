#!/usr/bin/python

import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address)

# Altitude in meters to calculate sea-level pressure
altitude = 27

try:
    temperature = data.temperature
    humidity = data.humidity
    hectopascals = data.pressure
    # Adjust pressure to sea level
    hectopascals = hectopascals*(1-(0.0065 * altitude)/(temperature + 0.0065 * altitude + 273.15))**(-5.257)
    print '{0:0.1f}\n{1}\n{2:0.2f}'.format(temperature, int(humidity), hectopascals)
except RuntimeError as e:
    print 'error\n{0}'.format(e)
except:
    print 'error\nFailed to read sensor data'
