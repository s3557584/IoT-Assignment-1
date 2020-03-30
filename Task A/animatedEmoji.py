from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
class AnimatedEmoji:
	def __init__(self, c1, c2):
		self.c1 = c1
		self.c2 = c2
	
	def displayEmoji(self):
		smiley_face = [
		self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1,
		self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1,
		self.c1, self.c2, self.c2, self.c1, self.c1, self.c2, self.c2, self.c1,
		self.c1, self.c2, self.c2, self.c1, self.c1, self.c2, self.c2, self.c1,
		self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1,
		self.c1, self.c2, self.c2, self.c1, self.c1, self.c2, self.c2, self.c1,
		self.c1, self.c1, self.c1, self.c2, self.c2, self.c1, self.c1, self.c1,
		self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1,
		]
		sad_face = [
		self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1,
		self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1,
		self.c1, self.c2, self.c2, self.c1, self.c1, self.c2, self.c2, self.c1,
		self.c1, self.c2, self.c2, self.c1, self.c1, self.c2, self.c2, self.c1,
		self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1,
		self.c1, self.c1, self.c1, self.c2, self.c2, self.c1, self.c1, self.c1,
		self.c1, self.c1, self.c2, self.c1, self.c1, self.c2, self.c1, self.c1,
		self.c1, self.c2, self.c1, self.c1, self.c1, self.c1, self.c2, self.c1,
		]
		surprised_face = [
		self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1,
		self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1, self.c1,
		self.c1, self.c2, self.c2, self.c1, self.c1, self.c2, self.c2, self.c1,
		self.c1, self.c2, self.c2, self.c1, self.c1, self.c2, self.c2, self.c1,
		self.c1, self.c1, self.c1, self.c2, self.c2, self.c1, self.c1, self.c1,
		self.c1, self.c1, self.c2, self.c1, self.c1, self.c2, self.c1, self.c1,
		self.c1, self.c1, self.c2, self.c1, self.c1, self.c2, self.c1, self.c1,
		self.c1, self.c1, self.c1, self.c2, self.c2, self.c1, self.c1, self.c1,
		]
		sense.set_pixels(smiley_face)
		sleep(3)
		sense.set_pixels(sad_face)
		sleep(3)
		sense.set_pixels(surprised_face)
		sleep(3)
	
	def getEmoji(self):
		return self.emoji
	
	def getColor1(self):
		return self.c1
	
	def getColor(self):
		return self.c2
