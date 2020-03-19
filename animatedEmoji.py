from emojiClass import Emoji
from sense_hat import SenseHat
y = (255, 255, 0) 
b = (0, 0, 0)
smiley_face = [
	y, y, y, y, y, y, y, y,
	y, y, y, y, y, y, y, y,
	y, b, b, y, y, b, b, y,
	y, b, b, y, y, b, b, y,
	y, y, y, y, y, y, y, y,
	y, b, b, y, y, b, b, y,
	y, y, y, b, b, y, y, y,
	y, y, y, y, y, y, y, y,
	]
sense = SenseHat()
emoji1 = Emoji(y, b, smiley_face)
emoji1.displayEmoji()
sense.clear()
