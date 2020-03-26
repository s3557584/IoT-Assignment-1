from sense_hat import SenseHat
import time
import random

sense = SenseHat()

class ElectronicDie:
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
    
    def __init__(self):
        pass
        
    def roll_dice(self):
        number = random.randint(1,6)
        if number == 1:
            sense.set_pixels(self.one_sided)
        elif number == 2:
            sense.set_pixels(self.two_sided)
        elif number == 3:
            sense.set_pixels(self.three_sided)
        elif number == 4:
            sense.set_pixels(self.four_sided)
        elif number == 5:
            sense.set_pixels(self.five_sided)
        elif number == 6:
            sense.set_pixels(self.six_sided)
        return number
