#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

seconden = 5

for i in range(0,seconden+1):
  sense.show_letter(str(seconden-i), text_colour=[0, 255, 0])
  sleep(1)
