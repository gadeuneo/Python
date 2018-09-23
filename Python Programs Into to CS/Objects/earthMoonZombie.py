


import sys
import pygame
import random
import math

# Moves the rectangle back onto the screen.
# Input: PyGame rect. Number. Number.
# Output: PyGame rect.
def clampRect(rect, width, height):
	new = rect
	if new.left < 0:
		new = new.move([-new.left, 0])
	if new.right > width:
		new = new.move([width - new.right, 0])
	if new.top < 0:
		new = new.move([0, -new.top])
	if new.bottom > height:
		new = new.move([0, height - new.bottom])
	return new

# Returns a new velocity for the zombie.
# Input: PyGame rect for zombie. Pair of numbers for zombie velocity. PyGame rect for human.
# Output: Pair of numbers for new zombie velocity.
def zombieVelocity(rect, vel, humRect):
	# Compute the zombie's and human's positions.
	pos = [(rect.left + rect.right) / 2.0, (rect.top + rect.bottom) / 2.0]
	humPos = [(humRect.left + humRect.right) / 2.0, (humRect.top + humRect.bottom) / 2.0]
	# Compute the zombie's speed and the distance to the human.
	speed = math.sqrt(vel[0]**2 + vel[1]**2)
	dist = (humPos[0] - pos[0])**2 + (humPos[1] - pos[1])**2
	# Alter the zombie's direction.
	if dist < 64**2:
		# The human is near here; aim toward it.
		dir = math.atan2(humPos[1] - pos[1], humPos[0] - pos[0])
	else:
		# The human is far away; aim randomly.
		dir = math.atan2(vel[1], vel[0])
		dir += random.uniform(-math.pi / 32.0, math.pi / 32.0)
	return [speed * math.cos(dir), speed * math.sin(dir)]

# Lets (i.e. forces) the player to evade some zombies.
# The player is controlled through the W, A, S, D keys.
def main():
	# Initialize PyGame and the drawing surface.
	pygame.init()
	width = 512
	height = 512
	surface = pygame.display.set_mode([width, height])
	# Initialize the player and zombie sprites.
	earth = pygame.image.load("earth32.bmp")
	earthRect = pygame.Rect(width / 2, height / 2, 32, 32)
	moon = pygame.image.load("moon32.bmp")
	aRect = pygame.Rect(width / 2 - 64, height / 2 - 64, 32, 32)
	aVel = [2, 1]
	bRect = pygame.Rect(width / 2 + 64, height / 2 + 64, 32, 32)
	bVel = [1, -2]
	while True:
		# Handle the user quitting or pressing a key.
		key = None
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				key = event.unicode
		# Move the player.
		if key == "w":
			earthRect = clampRect(earthRect.move([0, -20]), width, height)
		elif key == "a":
			earthRect = clampRect(earthRect.move([-20, 0]), width, height)
		elif key == "s":
			earthRect = clampRect(earthRect.move([0, 20]), width, height)
		elif key == "d":
			earthRect = clampRect(earthRect.move([20, 0]), width, height)
		# Move the zombies and update their velocities.
		aRect = aRect.move(aVel)
		aRect = clampRect(aRect, width, height)
		aVel = zombieVelocity(aRect, aVel, earthRect)
		bRect = bRect.move(bVel)
		bRect = clampRect(bRect, width, height)
		bVel = zombieVelocity(bRect, bVel, earthRect)
		# Draw.
		surface.fill([0, 0, 0])
		surface.blit(earth, earthRect)
		surface.blit(moon, aRect)
		surface.blit(moon, bRect)
		pygame.display.flip()

if __name__ == "__main__":
	main()