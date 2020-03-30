from sense_hat import SenseHat
from time import sleep

#Creating an object pointing to the SenseHat class
sense = SenseHat()

class AnimatedEmoji:
	
	#Constructor for the class
	#The parimeters are the colors for the emojis
	def __init__(self, c1, c2):
		self.c1 = c1
		self.c2 = c2
	
	#Function to display the emojis
	def displayEmoji(self):
		
		#The following code below are the pixle layout for the emojis
		#Layout for the smiley face emoji
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
		
		#Layout for the sad face emoji
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
		
		#Layout for the surprised face emoji
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
		
		#Displaying the 3 emojis with an interval of 3 seconds
		sense.set_pixels(smiley_face)
		sleep(3)
		sense.set_pixels(sad_face)
		sleep(3)
		sense.set_pixels(surprised_face)
		sleep(3)
