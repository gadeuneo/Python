


import sys
import pygame
import random
import math

def main():
	# Initialize PyGame and the drawing surface.
	pygame.init()
	width = 512
	height = 512
	surface = pygame.display.set_mode([width, height])
	# Initialize the Earth sprite.
	earth = pygame.image.load("earth32.bmp")
	rect = pygame.Rect(width / 2, height / 2, 32, 32)
	vel = [3, 2]
	while True:
		# Handle the user quitting.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		# Move Earth and update its velocity.
		rect = rect.move(vel)
		if rect.left < 0 or rect.right > width:
			vel[0] = -vel[0]
		if rect.top < 0 or rect.bottom > height:
			vel[1] = -vel[1]
		# Draw.
		surface.fill([0, 0, 0])
		surface.blit(earth, rect)
		pygame.display.flip()

if __name__ == "__main__":
	main()

