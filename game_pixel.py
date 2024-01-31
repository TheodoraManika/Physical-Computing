from picoed import *
import time

display.scroll("Start game")
score = 0

for y in range(7)
    for x in range(17):
        display.pixel(x, y, 50)
        if button_a.is_pressed:
            if x == 16: 
            score += 100
            elif x == 15: 
                score += 75
            else x == 14: 
                score += 50
            break
        time sleep(0.2)
    time.sleep(0.5)
    
display.scroll("Your score is: " + str(score)