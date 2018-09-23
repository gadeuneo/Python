import sys
import pygame
import random
import math


def dot(a,b):
    return sum( [a[i]*b[i] for i in range(len(b))] )

class Ball(object):
	
    def __init__(self, image, width, height, surface, velocity):
        self.image = image
        self.width = width
        self.height = height
        self.surface = surface
        self.velocity = velocity
        
    def getVelocity(self):
        return self.velocity
	
    def setVelocity(self, velocity):
        self.velocity = velocity
	
    def getPosition(self):
        return self.xy
	
    def setPosition(self, x, y):
        x = max(0, min(self.surface.get_width(), x))
        y = max(0, min(self.surface.get_height(), y))
        self.xy = [x, y]
	
    def draw(self):
        rect = pygame.Rect(self.xy[0] - self.width / 2.0, self.xy[1] - self.height / 2.0, self.width, self.height)
        self.surface.blit(self.image, rect)
    
    def updateVel(self):
        #print(self.getPosition())
        v = self.getVelocity()
        xy = self.getPosition()
        xy[0] += v[0]
        xy[1] += v[1]
        self.setPosition(xy[0], xy[1])
		
        if self.getPosition()[1] -8 < 0 or self.getPosition()[1] +8 > self.surface.get_height():
            oldvel = self.getVelocity()
            newvel = [oldvel[0], -(oldvel[1])]
            self.setVelocity(newvel)
        
        if self.getPosition()[0] -8 < 0 or self.getPosition()[0] +8 > self.surface.get_width():
            oldvel = self.getVelocity()
            newvel = [-oldvel[0]-1, oldvel[1]]
            self.setVelocity(newvel)
			#self.getVelocity()[0] = -self.getVelocity()[0]
		
    
    def bounce(self, Target):
        v = self.getVelocity()
        xy = self.getPosition()
        # Compute the distance to the target.
        print(v)
        d = [(Target.getPosition()[0] - xy[0]), (Target.getPosition()[1] - xy[1])]
        distSq = (Target.getPosition()[0] - xy[0])**2 + (Target.getPosition()[1] - xy[1])**2
        if distSq <= 16**2 and dot(d,v) > 0 and dot(d, Target.getVelocity()) < 0:
            scalar = 2.0 * (v[0] * d[0] + v[1] * d[1]) / (d[0] * d[0] + d[1] * d[1])
            self.velocity = [v[0] - scalar * d[0], v[1] - scalar * d[1]]
            scalar = 2.0 * (Target.getVelocity()[0] * d[0] + Target.getVelocity()[1] * d[1]) / (d[0] * d[0] + d[1] * d[1])
            Target.setVelocity([Target.getVelocity()[0] - scalar * d[0], Target.getVelocity()[1] - scalar * d[1]]) 

def moonBounce(n):
	# Initialize PyGame and the drawing surface.
    pygame.init()
    width = 366
    height = 734
    surface = pygame.display.set_mode([width, height])
	# Initialize the player and zombie sprites.
    ballList = []
    imList = [[pygame.image.load("whiteball.bmp")],[pygame.image.load("9ball.bmp")],[pygame.image.load("7ball.bmp")],[pygame.image.load("12ball.bmp")],[pygame.image.load("15ball.bmp")],[pygame.image.load("8ball.bmp")],[pygame.image.load("1ball.bmp")],[pygame.image.load("6ball.bmp")],[pygame.image.load("10ball.bmp")],[pygame.image.load("3ball.bmp")],[pygame.image.load("14ball.bmp")],[pygame.image.load("11ball.bmp")],[pygame.image.load("2ball.bmp")],[pygame.image.load("13ball.bmp")],[pygame.image.load("4ball.bmp")],[pygame.image.load("5ball.bmp")]]
    posList = [[183,550.5],[183,183.5],[171.68,172.18],[194.32,172.18],[160.36,160.86],[183,160.86],[205.64,160.86],[149.04,149.54],[171.68,149.54],[194.32,149.54],[216.96,149.54],[137.72,138.22],[160.36,138.22],[183,138.22],[205.64,138.22],[228.28,138.22]]
    velList = [[0,4],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    for i in range(n):
        e = Ball(imList[i][0], 16, 16, surface, velList[i])
        e.setPosition(posList[i][0],posList[i][1])
        ballList += [e]
    while True:
		# Handle the user quitting or pressing a key.
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.unicode
		#print(globe.getVelocity())
		#print(mon.getVelocity())
        n = len(ballList)
        
        
        for i in range(0,n-1):
            for j in range(i+1, n):
                ballList[i].bounce(ballList[j])
                
        for i in range(n):
            ballList[i].updateVel()
		#globe.bounce(mon)
		#mon.bounce(globe)
		# Draw.
        surface.fill([0, 0, 0])
        for i in range(n):
            ballList[i].draw()
        pygame.display.flip()

if __name__ == "__main__":
    moonBounce(16)
