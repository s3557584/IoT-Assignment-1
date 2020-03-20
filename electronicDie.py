from sense_hat import SenseHat
import time
import random

sense = SenseHat()

sense.clear()

sense.show_message("Shake to roll the dice")
y = (255, 255, 0)
b = (0, 0, 0)
g = (0, 255, 0)
r = (255, 0, 0)
blue = (0, 255, 255)
w = (255, 255, 255)
p = (128, 0, 128)

one_sided = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,y,y,b,b,b,
b,b,b,y,y,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

two_sided = [
b,b,b,b,b,b,b,b,
b,blue,blue,b,b,b,b,b,
b,blue,blue,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,blue,blue,b,
b,b,b,b,b,blue,blue,b,
b,b,b,b,b,b,b,b,
]

three_sided = [
g,g,b,b,b,b,b,b,
g,g,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,g,g,
b,b,b,b,b,b,g,g,
]

four_sided = [
b,b,b,b,b,b,b,b,
b,w,w,b,b,w,w,b,
b,w,w,b,b,w,w,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,w,w,b,b,w,w,b,
b,w,w,b,b,w,w,b,
b,b,b,b,b,b,b,b,
]

five_sided = [
p,p,b,b,b,b,p,p,
p,p,b,b,b,b,p,p,
b,b,b,b,b,b,b,b,
b,b,b,p,p,b,b,b,
b,b,b,p,p,b,b,b,
b,b,b,b,b,b,b,b,
p,p,b,b,b,b,p,p,
p,p,b,b,b,b,p,p,
]

six_sided = [
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
]

def roll_dice():
    
    number = random.randint(1,6)
    
    if number == 1:
        sense.set_pixels(one_sided)
    elif number == 2:
        sense.set_pixels(two_sided)
    elif number == 3:
        sense.set_pixels(three_sided)
    elif number == 4:
        sense.set_pixels(four_sided)
    elif number == 5:
        sense.set_pixels(five_sided)
    elif number == 6:
        sense.set_pixels(six_sided)

while True:
    a, b, c = sense.get_accelerometer_raw().values()

    a = abs(a)
    b = abs(b)
    c = abs(c)