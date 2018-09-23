import sys
import pygame
import random
import math
import time

# Bounces the Earth and moon around in a window, handling 
# collisions between them as if they have equal mass.
# Warning: Sometimes the bounce behaves crazily.
clock =pygame.time.Clock()
#clock =pygame.time.Clock()
#clock.tick(60)
def dot(a,b):
    return sum([a[i]*b[i] for i in range(len(b))])


def main():
	# Initialize PyGame and the drawing surface.
	pygame.init()
	width = 512
	height = 512
	surface = pygame.display.set_mode([width, height])
	# Initialize the Earth and moon sprites.
	earth = pygame.image.load("earth32.bmp")
	earthRect = pygame.Rect(width / 2, height / 2, 32, 32)
	earthVel = [7, 6]
	moon = pygame.image.load("moon32.bmp")
	moonRect = pygame.Rect(width / 2 - 64, height / 2 - 64, 32, 32)
	moonVel = [9, 4]
	
	while True:
		# Handle the user quitting.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		# Move Earth and update its velocity.
		earthRect = earthRect.move(earthVel)
		clock.tick(60)
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
		if (d[0] * d[0] + d[1] * d[1] <= 32 * 32) and dot(d,earthVel) >0 and dot(d, moonVel) < 0:
			# They have collided; bounce them off each other.
			scalar = 2.0 * (earthVel[0] * d[0] + earthVel[1] * d[1]) / (d[0] * d[0] + d[1] * d[1])
			earthVel = [earthVel[0] - scalar * d[0], earthVel[1] - scalar * d[1]]
			scalar = 2.0 * (moonVel[0] * d[0] + moonVel[1] * d[1]) / (d[0] * d[0] + d[1] * d[1])
			moonVel = [moonVel[0] - scalar * d[0], moonVel[1] - scalar * d[1]]
		# Draw.
		surface.fill([0, 0, 0])
		surface.blit(earth, earthRect)
		surface.blit(moon, moonRect)
		pygame.display.flip()

if __name__ == "__main__":
	main()


