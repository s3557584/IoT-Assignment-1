from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
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
sad_face = [
	y, y, y, y, y, y, y, y,
	y, y, y, y, y, y, y, y,
	y, b, b, y, y, b, b, y,
	y, b, b, y, y, b, b, y,
	y, y, y, y, y, y, y, y,
	y, y, y, b, b, y, y, y,
	y, y, b, y, y, b, y, y,
	y, b, y, y, y, y, b, y,
	]
surprised_face = [
	y, y, y, y, y, y, y, y,
	y, y, y, y, y, y, y, y,
	y, b, b, y, y, b, b, y,
	y, b, b, y, y, b, b, y,
	y, y, y, b, b, y, y, y,
	y, y, b, y, y, b, y, y,
	y, y, b, y, y, b, y, y,
	y, y, y, b, b, y, y, y,
	]
sense.set_pixels(smiley_face)
sleep(3)
sense.set_pixels(sad_face)
sleep(3)
sense.set_pixels(surprised_face)
sleep(3)
sense.clear()