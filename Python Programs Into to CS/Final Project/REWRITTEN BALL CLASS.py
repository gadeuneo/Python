
import sys, pygame, random, math, time


mod = (lambda v: sqrt(v[0]**2 + v[1]**2))

def dot(a,b):
	return sum([a[i]*b[i] for i in range(len(b))])

class Ball(object):
	def __init__(self, image, width, height, surface, velocity):
		self.image = image
		self.width = width
		self.height = height
		self.surface = surface
		self.velocity = velocity
		
	def setPosition(self, x, y):
		x = max(0, min(self.surface.get_width(), x))
		y = max(0, min(self.surface.get_height(), y))
		self.xy = [x,y]
	def getPosition(self):
		return self.xy
	
	def setVelocity(self, velocity):
		self.velocity = velocity
	def getVelocity(self):
		return self.velocity
	
	def draw(self):
		rect = pygame.Rect(self.xy[0] - self.width / 2.0, self.xy[1] - self.height / 2.0, self.width, self.height)
		self.surface.blit(self.image, rect)
	
	def decelerate(self, friction):
		if mod(self.velocity) == [0.0,0.0]:
			self.velocity = [0.0,0.0]
		else:
			self.velocity[0] = self.velocity[0] - friction * self.velocity[0] / mod(self.velocity)
			self.velocity[1] = self.velocity[1] - friction * self.velocity[1] / mod(self.velocity)

	def reflect(self):
		reflected = False
		if self.getPosition[0] - 8 < 0 or self.getPosition[0] + 8 > self.surface.get_width():
			reflected = True
			self.velocity[0] = -self.velocity[0]
			if self.getPosition[0]-8 < 0:
				self.setPosition([self.getPosition[0], self.getPosition[1]])
			else:
				self.setPosition([self.surface.get_width() - self.getPosition[0], self.getPosition[1]])
		elif self.getPosition[1] -8 < 0 or self.getPosition[1] + 8 > self.surface.get_height:
			reflected = True
			self.velocity[1] = -self.velocity[1]
			if self.getPosition[1] - 8 < 0:
				self.setPosition([self.getPosition[0], self.getPosition[1]])
			else:
				self.setPosition([self.getPosition[0], self.surface.get_height - self.getPosition[1]])
		
	def collide(self, other):
		v = self.getVelocity()
		xy = self.getPosition()
		d = [(other.getPosition()[0] - xy[0]), (other.getPosition()[1] - xy[1])]
		distSq = (other.getPosition()[0] - xy[0])**2 + (other.getPosition()[1] - xy[1])**2
		if distSq <= 16**2 and dot(d,v) > 0 and dot(d, other.getVelocity) < 0:
			scalar = 2.0 * (v[0] * d[0] + v[1]*d[1]) / (d[0]**2 + d[1]**2)
			self.velocity = [v[0] - scalar * d[0], v[1] - scalar * d[1]]
			scalar = 2.0 * (other.getVelocity()[0] * d[0] + other.getVelocity()[1]*d[1]) / (d[0]**2 + d[1]**2)
			other.velocity = [other.getVelocity()[0] - scalar * d[0], other.getVelocity()[1] - scalar * d[1]]
			
def main(n):
	pygame.init()
	width = 366
	height = 734
	
	surface = pygame.display.set_mode([width, height])
	
	ballList = []
	
	imList = [[pygame.image.load("whiteball.bmp")],[pygame.image.load("9ball.bmp")],[pygame.image.load("7ball.bmp")],[pygame.image.load("12ball.bmp")],[pygame.image.load("15ball.bmp")],[pygame.image.load("8ball.bmp")],[pygame.image.load("1ball.bmp")],[pygame.image.load("6ball.bmp")],[pygame.image.load("10ball.bmp")],[pygame.image.load("3ball.bmp")],[pygame.image.load("14ball.bmp")],[pygame.image.load("11ball.bmp")],[pygame.image.load("2ball.bmp")],[pygame.image.load("13ball.bmp")],[pygame.image.load("4ball.bmp")],[pygame.image.load("5ball.bmp")]]
	
	posList = [[183,550.5],[183,183.5],[171.68,172.18],[194.32,172.18],[160.36,160.86],[183,160.86],[205.64,160.86],[149.04,149.54],[171.68,149.54],[194.32,149.54],[216.96,149.54],[137.72,138.22],[160.36,138.22],[183,138.22],[205.64,138.22],[228.28,138.22]]
	
	velList = [[0,-3],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]
	
	for i in range(n):
		b = Ball(imList[i], 16,16, surface, velList[i])
		b.setPosition(posList[i][0], posList[i][1])
		ballList += [b]
		
	while True:
		key = None
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				key = event.unicode
		s = len(ballList)
		
		for k in range(s):
			for i in range(s):
				for j in range(i+1,s):
					ballList[i].collide(ballList[j])
			for u in range(s):
				ballList[u].reflect
		
		surface.fill([10,108,13])
		for m in range(n):
			ballList[m].draw()
		pygame.display.flip()
		
if __name__ == "__main__":
	main(16)