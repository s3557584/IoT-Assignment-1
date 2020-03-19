from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
class Emoji:
	def __init__(self, c1, c2, emoji):
		self.c1 = c1
		self.c2 = c2
		self.emoji = emoji
	
	def displayEmoji(self):
		sense.set_pixels(self.emoji)
		sleep(3)
	
	def getEmoji(self):
		return self.emoji
	
	def getColor1(self):
		return self.c1
	
	def getColor(self):
		return self.c2