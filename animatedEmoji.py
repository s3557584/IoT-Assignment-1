from emojiClass import Emoji
from sense_hat import SenseHat
yellow = (255, 255, 0)
white = (255, 255, 255)
blue = (0, 255, 255)
b = (0, 0, 0)
sense = SenseHat()
emoji1 = Emoji(yellow, b)
emoji2 = Emoji(white, b)
emoji3 = Emoji(blue, b)
emoji1.displayEmoji()
emoji2.displayEmoji()
emoji3.displayEmoji()
sense.clear()