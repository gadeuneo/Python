import sys, pygame, random, math, time

clock = pygame.time.Clock()

def dot(a,b):
	return sum([a[i]*b[i] for i in range(len(b))])

class Image(object):
	def __init__(self, image, width, height, surface, velocity): #takes in an image to be drawn, the image's width, the image's height, and the surface for the image to be drawn on
		self.image = image #defines the image that is to be drawn
		self.width = width #defines the width of the image
		self.height = height #defines the height of the image
		self.surface = surface #defines the surface on which the image is to be drawn
		self.velocity = velocity
	
	def setVelocity(self, velocity): #sets the VELOCITY of an object given an inital velocity with an X-VELOCITY and a Y-VELOCITY
		self.velocity = velocity
	def getVelocity(self):
		return self.velocity
	
	def setPosistion(self, x, y): #sets the position of an object given an x and y coordinate pair
		x = max(0,min(self.surface.get_width(),x)) #Sets the x coordinate postion of the object
		y = max(0,min(self.surface.get_height(),y)) #Set the y coordinate postion of the object
		self.xy = [x,y] #Coordinate of the object
	def getPosition(self):
		return self.xy #returns the coordinate of the object
		
	def draw(self): #draws the image
		rect = pygame.Rect(self.xy[0] - self.width / 2.0, self.xy[1] - self.height / 2.0, self.width, self.height) #draws the rectange for the image to be placed into
		self.surface.blit(self.image,rect) #draws the rectangle on the surface
	
	'''def bounce(self, other):
		v = self.getVelocity'''

#class Ball(Image):	
	
	def bounce(self,other):
		#Updates the position based on the OLD VELOCITY
		v = self.getVelocity()
		xy = self.getPosition()
		xy[0] += v[0]
		xy[1] += v[1]
		self.setPosistion(xy[0],xy[1])
		#Bounces off of wall
		if self.getPosition()[0] -16 < 0 or self.getPosition()[0] + 16 > self.surface.get_width():
			oldv = self.getVelocity()
			newv = [-oldv[0], oldv[1]]
			self.setVelocity(newv)
		elif self.getPosition()[1] -16 < 0 or self.getPosition()[1] + 16 > self.surface.get_height():
			oldv = self.getVelocity()
			newv = [oldv[0],-oldv[1]]
			self.setVelocity(newv)
		
		#Computes the distance between the objects and checks to see if they are within 32 pixels of each other
		d = [(other.getPosition()[0] - xy[0]), (other.getPosition()[1] - xy[1])]
		distSq = (other.getPosition()[0] - xy[0])**2 + (other.getPosition()[1]-xy[1])**2
		if distSq <= 32**2 and dot(d,v) > 0 and dot(d,other.getVelocity()) > 0:
			scalar = 2.0 * (v[0]*d[0]+v[1]*d[1]) / (d[0]**2 + d[1]**2)
			self.velocity = [v[0] - scalar*d[0],v[1]-scalar*d[1]]
			scalar = 2.0 * (other.getVelocity()[0] * d[0] + other.getVelocity()[1] * d[1]) / (d[0]**2 + d[1]**2)
			other.velocity = [other.getVelocity()[0]-scalar*d[0], other.getVelocity()[1] - scalar*d[1]]
			

		
def main(n):
		#Initialize PyGame and the drawing surface
		pygame.init()
		width = 400
		height = 500
		surface = pygame.display.set_mode([width,height])
		#Initialize ball images
		ball = pygame.image.load("earth32.bmp")
		ballList = []
		for i in range(n):
			b = Image(ball, 32, 32, surface, [2,4])
			b.setPosistion(random.randint(1,width-1,), random.randint(1,height-1))
			ballList.append(b)
		while True:
			#Handle User quitting or pressing a key.
			key = None
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					key = event.unicode
			for j in range(n):
				#for k in range(n):
				ballList[i].bounce(ballList[i])
			surface.fill([0,0,0])
			for m in range(n):
				ballList[m].draw()
				clock.tick(60)
			pygame.display.flip()
			
if __name__ == "__main__":
	main(4)