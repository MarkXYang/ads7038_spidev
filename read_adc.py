#!/bin/python

import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)

rsp = spi.xfer2([0x10, 0x10, 0x00])
time.sleep(0.1)
rsp = spi.xfer2([0x10, 0x05, 0x00])
print("SEQUENCE_CFG: ".format(rsp[0]))
print(rsp[0])
time.sleep(0.1)
rsp = spi.xfer2([0x10, 0x04, 0x00])
print('PIN_CFG: '.format(rsp[0]))
print(rsp[0])
time.sleep(0.1)
rsp = spi.xfer2([0x10, 0x11, 0x00])
print('OPMODE_CFG: '.format(rsp[0]))
print(rsp[0])
time.sleep(0.1)
rsp = spi.xfer2([0x10, 0x02, 0x00])
print('MANUAL_CH_SEL: '.format(rsp[0]))
print(rsp[0])
rsp = spi.xfer2([0x10, 0x00, 0x00])
print('DATA_CFG:')
print(rsp)
val = (rsp[0] & ~0x30) | (1 << 4)
print(val)

rsp = spi.xfer2([0x10, 0x11, 0x00])
time.sleep(0.1)
# 4-bit channel ID is appended to ADC data
rsp = spi.xfer2([0x08, 0x02, val])
print('Channel ID reg:')
print(rsp[0])

for i in range(8):
	rsp = spi.xfer2([0x08, 0x11, i])
	rsp = spi.xfer2([0x08, 0x11, i])
	rsp = spi.xfer2([0x08, 0x11, i])
	adc = (rsp[0] << 8) + rsp[1]
	print('Channel_{}: 0x{:04x}'.format(i, adc))

spi.close()

