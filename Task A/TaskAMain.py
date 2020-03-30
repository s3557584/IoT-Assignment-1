from animatedEmoji import AnimatedEmoji
from sense_hat import SenseHat
yellow = (255, 255, 0)
white = (255, 255, 255)
blue = (0, 255, 255)
b = (0, 0, 0)
sense = SenseHat()
emoji1 = AnimatedEmoji(yellow, b)
emoji2 = AnimatedEmoji(white, b)
emoji3 = AnimatedEmoji(blue, b)
emoji1.displayEmoji()
emoji2.displayEmoji()
emoji3.displayEmoji()
sense.clear()
