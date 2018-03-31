import sys
import pygame
import random
import math

class Ball(object):
	
	def __init__(self, image, width, height, surface, x, y):
		self.image = image
		self.width = width
		self.height = height
		self.surface = surface
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
	
	def getPosition(self):
		return self.xy
	
	def setPosition(self, x, y):
		x = max(0, min(self.surface.get_width(), x))
		y = max(0, min(self.surface.get_height(), y))
		self.xy = [x, y]
	
	def draw(self):
		rect = pygame.Rect(self.xy[0] - self.width / 2.0, self.xy[1] - self.height / 2.0, self.width, self.height)
		self.surface.blit(self.image, rect)
    
    def bounce(self, Target):
        v = self.getVelocity()
		xy = self.getPosition()
		xy[0] += v[0]
		xy[1] += v[1]
		self.setPosition(xy[0], xy[1])
		# Compute the distance to the target.
		dist = [(Target.getPosition[0] - xy[0]), (Target.getPosition[1] - xy[1])]
        distSq = (Target.getPosition[0] - xy[0])**2 + (Target.getPosition[1] - xy[1])**2
        if distSq < 32**2 and dot(d,v) >0 and dot(d, Target.getVelocity) < 0:
			scalar = 2.0 * (v[0] * d[0] + v[1] * d[1]) / (d[0] * d[0] + d[1] * d[1])
			v = [v[0] - scalar * d[0], v[1] - scalar * d[1]]
			scalar = 2.0 * (Target.getVelocity[0] * d[0] + Target.getVelocity[1] * d[1]) / (d[0] * d[0] + d[1] * d[1])
			Target.getVelocity = [Target.getVelocity[0] - scalar * d[0], Target.getVelocity[1] - scalar * d[1]]