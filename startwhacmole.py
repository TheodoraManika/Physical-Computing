from picoed import *
import time
import random


left_side = Image(
            "99999000000000000:"
            "90909000000000000:"
            "90909000000000000:"
            "99999000000000000:"
            "00000000000000000:"
            "99999000000000000:"
            "99999000000000000:")


right_side = Image(
            "00000000000099999:"
            "00000000000090909:"
            "00000000000090909:"
            "00000000000099999:"
            "00000000000000000:"
            "00000000000099999:"
            "00000000000099999:")

both_sides = Image(
            "99999000000099999:"
            "90909000000090909:"
            "90909000000090909:"
            "99999000000099999:"
            "00000000000000000:"
            "99999000000099999:"
            "99999000000099999:")

score = 0
lives = 3
images = [left_side, right_side, both_sides]
while True:
    side = random.randint(0,2)
    display.show(images[side])
    t = random.randrange(300, 600)
    time.sleep(t)