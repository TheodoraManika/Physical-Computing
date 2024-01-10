from picoed import *
import time

x = 8
y = 3
display.pixel(x, y, 50)
time.sleep(0.2)

while True:
    if button_a.is_pressed():
        display.pixel(x, y, 0)
        x = x - 1
        display.pixel(x, y, 50)
        while button_a.is_pressed():pass
    elif button_b.is_pressed():
        display.pixel(x, y, 0)
        x = x + 1
        display.pixel(x, y, 50)
        while button_b.is_pressed():pass