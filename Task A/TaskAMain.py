from animatedEmoji import AnimatedEmoji
from sense_hat import SenseHat

#Color variables for yellow, white, blue and blank
yellow = (255, 255, 0)
white = (255, 255, 255)
blue = (0, 255, 255)
b = (0, 0, 0)

#Creating an object pointing to the SenseHat class
sense = SenseHat()

#Creating 3 diffrent objects to the AnimatedEmoji class
#1st object with the color yellow
emoji1 = AnimatedEmoji(yellow, b)

#2nd object with the color white
emoji2 = AnimatedEmoji(white, b)

#3rd object with the color blue
emoji3 = AnimatedEmoji(blue, b)

#Calling the displayEmoji() function for each object created
emoji1.displayEmoji()
emoji2.displayEmoji()
emoji3.displayEmoji()

#Clearing the LED display of sensehat after finish displaying
sense.clear()
