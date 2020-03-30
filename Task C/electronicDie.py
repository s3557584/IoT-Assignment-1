from sense_hat import SenseHat
import time
import random

#Creating an object pointing to the SenseHat class
sense = SenseHat()

class ElectronicDie:
    
    #Colors for each value of the die
    y = (255, 255, 0)
    d = (0, 0, 0)
    g = (0, 255, 0)
    r = (255, 0, 0)
    b = (0, 255, 255)
    w = (255, 255, 255)
    p = (128, 0, 128)
    
    #Pixel layout for each side of the die
    #One, color: yellow
    one_sided = [
        d,d,d,d,d,d,d,d,
        d,d,d,d,d,d,d,d,
        d,d,d,d,d,d,d,d,
        d,d,d,y,y,d,d,d,
        d,d,d,y,y,d,d,d,
        d,d,d,d,d,d,d,d,
        d,d,d,d,d,d,d,d,
        d,d,d,d,d,d,d,d,
    ]
    
    #Two, color: blue
    two_sided = [
        d,d,d,d,d,d,d,d,
        d,b,b,d,d,d,d,d,
        d,b,b,d,d,d,d,d,
        d,d,d,d,d,d,d,d,
        d,d,d,d,d,d,d,d,
        d,d,d,d,d,b,b,d,
        d,d,d,d,d,b,b,d,
        d,d,d,d,d,d,d,d,
    ]
    
    #Three, color: green
    three_sided = [
        g,g,d,d,d,d,d,d,
        g,g,d,d,d,d,d,d,
        d,d,d,d,d,d,d,d,
        d,d,d,g,g,d,d,d,
        d,d,d,g,g,d,d,d,
        d,d,d,d,d,d,d,d,
        d,d,d,d,d,d,g,g,
        d,d,d,d,d,d,g,g,
    ]
    
    #Four, color: white
    four_sided = [
        d,d,d,d,d,d,d,d,
        d,w,w,d,d,w,w,d,
        d,w,w,d,d,w,w,d,
        d,d,d,d,d,d,d,d,
        d,d,d,d,d,d,d,d,
        d,w,w,d,d,w,w,d,
        d,w,w,d,d,w,w,d,
        d,d,d,d,d,d,d,d,
    ]
    
    #Five, color: purple
    five_sided = [
        p,p,d,d,d,d,p,p,
        p,p,d,d,d,d,p,p,
        d,d,d,d,d,d,d,d,
        d,d,d,p,p,d,d,d,
        d,d,d,p,p,d,d,d,
        d,d,d,d,d,d,d,d,
        p,p,d,d,d,d,p,p,
        p,p,d,d,d,d,p,p,
    ]
    
    #Six, color: red
    six_sided = [
        r,r,d,d,d,d,r,r,
        r,r,d,d,d,d,r,r,
        d,d,d,d,d,d,d,d,
        r,r,d,d,d,d,r,r,
        r,r,d,d,d,d,r,r,
        d,d,d,d,d,d,d,d,
        r,r,d,d,d,d,r,r,
        r,r,d,d,d,d,r,r,
    ]
    
    #Empty constructor
    def __init__(self):
        pass
    
    #This function generates a number from 1 to 6
    #And displays them through the sensehat in a form of a die
    def roll_dice(self):
        
        #Generate a random number from 1 to 6
        number = random.randint(1,6)
        
        #Display the numbers through the sensehat 
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
