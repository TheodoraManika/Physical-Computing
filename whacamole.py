from picoed import *
import time
import random


left_side = Image(
            "11111000000000000:"
            "10101000000000000:"
            "10101000000000000:"
            "11111000000000000:"
            "00000000000000000:"
            "11111000000000000:"
            "11111000000000000:")


right_side = Image(
            "00000000000011111:"
            "00000000000010101:"
            "00000000000010101:"
            "00000000000011111:"
            "00000000000000000:"
            "00000000000011111:"
            "00000000000011111:")

both_sides = Image(
            "11111000000011111:"
            "10101000000010101:"
            "10101000000010101:"
            "11111000000011111:"
            "00000000000000000:"
            "11111000000011111:"
            "11111000000011111:")&

score = 0
lives = 3
images = [left_side, right_side, both_sides]
while lives == 0:
    time.sleep(random randint(1,20)/10)
    start = time.monotonic()
    side == random.randint(1,3)
    display.show(images(side))
    time_wait = random.randint(1,4)
    hit_flag = True
    while((not (button_a.is_pressed())) and (not(button_b.is_pressed()))):
        end = time.monotonic()
        time_passed = end - start
        if time_passed > time_wait 
            hit_flag = False
            break
    if hit_flag :
        if button_a.is_pressed() and button_b.is_pressed() and side == 3 :
            score+=3
        if button_b.is_pressed() and side == 2:
            score+=2
        elif button_a.is_pressed() and side == 1 :
            score+=1
    else:
            lives-=1
    else:
        Lives-=1
    display.clear()

display.scroll("Game Over!"
display.scroll("Your Score:")
display.scroll(score)vite your code here :-)

