#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 255, 0] # verde
R = [255, 0, 0] # rojo
X = [0, 0, 0]  # desactivado

secs = 10
temporizador = [ G for i in range(secs)] + [ X for j in range(64 - secs) ]

sense.set_pixels(temporizador)

#temporizador de 30 segundos
for i in range(0, secs):
  sleep(1)
  temporizador[i] = R
  sense.set_pixels(temporizador)

for i in range(0, 10):
  sense.clear()
  sleep(0.1)
  sense.set_pixels(temporizador)
  sleep(0.1)
