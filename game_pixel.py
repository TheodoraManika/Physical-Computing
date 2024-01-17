from picoed import *
import time


for y in range(7):
    for x in range(17):
        display.pixel(x, y, 50)
        if button_a.is_pressed():
            break
        time.sleep(0.2)
    time.sleep(0.5)