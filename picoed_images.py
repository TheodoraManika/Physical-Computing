from picoed import *
import time

while True:
    display.scroll("Start")
    time.sleep(2)
    display.show(Image.PEEK_LEFT)
    time.sleep(2)
    display.show(Image.PEEK_RIGHT)
    time.sleep(2)
    display.show(Image.SUPERCILIOUS_LOOK)
    time.sleep(2)
    display.show(Image.EXCITED)
    time.sleep(2)
    display.scroll("End")
    time.sleep(2)
    