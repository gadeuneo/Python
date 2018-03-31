


import sys
import pygame
import random
import math

# Bounces the Earth and moon around in a window, handling 
# collisions between them as if they have equal mass, but also incorporating
# Newtonian gravity, where the Earth's mass is 64 times that of the moon.
# Warning: Results are crummy.
def main():
	# Initialize PyGame and the drawing surface.
	pygame.init()
	width = 512
	height = 512
	surface = pygame.display.set_mode([width, height])
	# Initialize the Earth and moon sprites.
	earth = pygame.image.load("earth32.bmp")
	earthRect = pygame.Rect(width / 2, height / 2, 32, 32)
	earthVel = [3, 2]
	moon = pygame.image.load("moon32.bmp")
	moonRect = pygame.Rect(width / 2 - 64, height / 2 - 64, 32, 32)
	moonVel = [2, 4]
	while True:
		# Handle the user quitting.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		# Move Earth and update its velocity.
		earthRect = earthRect.move(earthVel)
		if earthRect.left < 0 or earthRect.right > width:
			earthVel[0] = -earthVel[0]
		if earthRect.top < 0 or earthRect.bottom > height:
			earthVel[1] = -earthVel[1]
		# Move the moon and update its velocity.
		moonRect = moonRect.move(moonVel)
		if moonRect.left < 0 or moonRect.right > width:
			moonVel[0] = -moonVel[0]
		if moonRect.top < 0 or moonRect.bottom > height:
			moonVel[1] = -moonVel[1]
		# Test whether Earth and its moon have collided, by testing
		# whether their centers are within 32 of each other.
		e = [(earthRect.right + earthRect.left) / 2.0, (earthRect.top + earthRect.bottom) / 2.0]
		m = [(moonRect.right + moonRect.left) / 2.0, (moonRect.top + moonRect.bottom) / 2.0]
		d = [m[0] - e[0], m[1] - e[1]]
		if d[0] * d[0] + d[1] * d[1] <= 32 * 32:
			# They have collided; bounce them off each other (with equal mass).
			scalar = 2.0 * (earthVel[0] * d[0] + earthVel[1] * d[1]) / (d[0] * d[0] + d[1] * d[1])
			earthVel = [earthVel[0] - scalar * d[0], earthVel[1] - scalar * d[1]]
			scalar = 2.0 * (moonVel[0] * d[0] + moonVel[1] * d[1]) / (d[0] * d[0] + d[1] * d[1])
			moonVel = [moonVel[0] - scalar * d[0], moonVel[1] - scalar * d[1]]
		# Accelerate due to Newtonian gravity, 
		# assuming Earth is 64 times as massive as the moon.
		scalar = 0.1 / (d[0] * d[0] + d[1] * d[1])
		earthVel = [earthVel[0] + scalar * d[0], earthVel[1] + scalar * d[1]]
		moonVel = [moonVel[0] - 64.0 * scalar * d[0], moonVel[1] - 64.0 * scalar * d[1]]
		# Draw.
		surface.fill([0, 0, 0])
		surface.blit(earth, earthRect)
		surface.blit(moon, moonRect)
		pygame.display.flip()

if __name__ == "__main__":
	main()

