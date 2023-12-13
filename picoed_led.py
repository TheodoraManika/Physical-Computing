from picoed import *
import time

led.on()
time.sleep(1)
led.off()

while True:
    led.toggle()
    time.sleep(1)