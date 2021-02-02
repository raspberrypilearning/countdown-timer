#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 255, 0]  # groen
R = [255, 0, 0] # rood
X = [0, 0, 0]  # uit

seconden = 10
timer = [ G for i in range(seconden)] + [ X for j in range(64 - seconden) ]

sense.set_pixels(timer)

# 30 seconden timer
for i in range(0, seconden):
  sleep(1)
  timer[i] = R
  sense.set_pixels(timer)

for i in range(0, 10):
  sense.clear()
  sleep(0.1)
  sense.set_pixels(timer)
  sleep(0.1)
