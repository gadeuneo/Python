


import sys
import pygame
import random
import math

class Actor(object):
	
	def __init__(self, image, width, height, surface):
		self.image = image
		self.width = width
		self.height = height
		self.surface = surface
		self.setPosition(0.0, 0.0)
	
	def getPosition(self):
		return self.xy
	
	def setPosition(self, x, y):
		x = max(0, min(self.surface.get_width(), x))
		y = max(0, min(self.surface.get_height(), y))
		self.xy = [x, y]
	
	def draw(self):
		rect = pygame.Rect(self.xy[0] - self.width / 2.0, self.xy[1] - self.height / 2.0, self.width, self.height)
		self.surface.blit(self.image, rect)

class Human(Actor):
	
	def move(self, key):
		xy = self.getPosition()
		if key == "w":
			xy[1] -= 20
		elif key == "a":
			xy[0] -= 20
		elif key == "s":
			xy[1] += 20
		elif key == "d":
			xy[0] += 20
		self.setPosition(xy[0], xy[1])

class Zombie(Actor):
	
	def __init__(self, image, width, height, surface):
		super().__init__(image, width, height, surface)
		self.setSpeed(2.0)
		self.setDirection(random.uniform(0, 2.0 * math.pi))
	
	def getSpeed(self):
		return self.speed
	
	def setSpeed(self, speed):
		self.speed = speed
	
	def getDirection(self):
		return self.dir
	
	def setDirection(self, direction):
		self.dir = direction
	
	def getVelocity(self):
		v0 = self.speed * math.cos(self.dir)
		v1 = self.speed * math.sin(self.dir)
		return [v0, v1]
	
	def setVelocity(self, v):
		self.dir = math.atan2(v[1], v[0])
		self.speed = math.sqrt(v[0]**2 + v[1]**2)
	
	def updatePositionVelocity(self, xyTarget):
		# Update the position based on the old velocity.
		v = self.getVelocity()
		xy = self.getPosition()
		xy[0] += v[0]
		xy[1] += v[1]
		self.setPosition(xy[0], xy[1])
		# Compute the distance to the target.
		distSq = (xyTarget[0] - xy[0])**2 + (xyTarget[1] - xy[1])**2
		if distSq < 64**2:
			# The target is near here; aim toward it.
			self.setDirection(math.atan2(xyTarget[1] - xy[1], xyTarget[0] - xy[0]))
		else:
			# The human is far away; aim randomly.
			self.setDirection(self.getDirection() + random.uniform(-math.pi / 32.0, math.pi / 32.0))

# Lets (i.e. forces) the player to evade some zombies.
# The player is controlled through the W, A, S, D keys.
# Input: None.
# Output: None.
def zombies():
	# Initialize PyGame and the drawing surface.
	pygame.init()
	width = 512
	height = 512
	surface = pygame.display.set_mode([width, height])
	# Initialize the player and zombie sprites.
	earth = pygame.image.load("earth32.bmp")
	player = Human(earth, 32, 32, surface)
	moon = pygame.image.load("moon32.bmp")
	a = Zombie(moon, 32, 32, surface)
	a.setPosition(width / 4, height * 3 / 4)
	b = Zombie(moon, 32, 32, surface)
	b.setPosition(width * 3 / 4, height / 4)
	while True:
		# Handle the user quitting or pressing a key.
		key = None
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				key = event.unicode
		# Move player and zombies.
		player.move(key)
		a.updatePositionVelocity(player.getPosition())
		b.updatePositionVelocity(player.getPosition())
		# Draw.
		surface.fill([0, 0, 0])
		player.draw()
		a.draw()
		b.draw()
		pygame.display.flip()

if __name__ == "__main__":
	zombies()

