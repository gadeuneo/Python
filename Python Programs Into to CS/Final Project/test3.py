import sys
import pygame
import random
import math
import time

class PointOp(object):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def dot(self):
        total = 0
        for i in range(len(self.point1)):
            total = total + self.point1[i] * self.point2[i]
        return total

    def sub(self):
        total = []
        for i in range(len(self.point2)):
            total += [self.point1[i] - self.point2[i]]
        return total
    
    def add(self):
        total = []
        for i in range(len(self.point2)):
            total += [self.point1[i] + self.point2[i]]
        return total
    
    def mult(self):
        total = []
        for i in range(len(self.point2)):
            total += [self.point1*self.point2[i]]
        return total
    
    def distSq(self):
        return ((self.point1[0] - self.point2[0])**2 + (self.point1[1] - self.point2[1])**2)
    
    def dist(self):
        return [(self.point2[0] - self.point1[0]), (self.point2[1] - self.point1[1])]

class Drawer(object):
    def __init__(self, image, surface):
        self.image = image
        self.surface = surface

class Background(Drawer):
    
    def draw(self):
        rect = pygame.Rect(0, 0, 426, 794)
        self.surface.blit(self.image, rect)

class Ball(Drawer):
    def __init__(self, image, width, height, surface, velocity):
        super().__init__(image, surface)
        self.width = width
        self.height = height
        self.velocity = velocity
	
    def draw(self):
        rect = pygame.Rect(self.xy[0] - self.width / 2.0, self.xy[1] - self.height / 2.0, self.width, self.height)
        self.surface.blit(self.image, rect)
    
    def getVelocity(self):
        return self.velocity
    
    def setVelocity(self, velocity):
        self.velocity = velocity
	
    def getPosition(self):
        return self.xy
	
    def setPosition(self,x,y):
        #x = max(30, min(396, x))
        #y = max(30, min(764, y))
        self.xy = [x,y]
		
    def updatePos(self, timeStep, pointList):
        #print(self.getPosition())
        #implement slowing down
        v = self.getVelocity()
        xy = self.getPosition()
        xy[0] += v[0]*timeStep# multiply this and the xy func below by a decreasing somthing in proportion to power
        xy[1] += v[1]*timeStep
        self.setPosition(xy[0], xy[1])
		
        if self.getPosition()[0] > 51 and self.getPosition()[0] < 396:
            if self.getPosition()[1] -8 < 30 or self.getPosition()[1] +8 > 764:
                oldvel = self.getVelocity()
                newvel = [oldvel[0], -(oldvel[1])]
                self.setVelocity(newvel)
        
        if self.getPosition()[1] > 51 and self.getPosition()[1] < 378 or self.getPosition()[1] > 413 and self.getPosition()[1] < 764:
            if self.getPosition()[0] -8 < 30 or self.getPosition()[0] +8 > 396:
                oldvel = self.getVelocity()
                newvel = [-oldvel[0], oldvel[1]]
                self.setVelocity(newvel)
			
        
        nearestPoint = []
        for i in range(len(pointList)-1):
            a = pointList[i]
            b = pointList[i+1]
            c = self.getPosition()
        
            t = (PointOp(PointOp(b,c).sub(),PointOp(a,c).sub()).dot()/PointOp(PointOp(b,a).sub(),PointOp(b,a).sub()).dot()) #this is how far down the line the ball is going towards
            if t > 0 and t < 1:
                nearestPoint = (PointOp(a,PointOp(t,PointOp(b,a).sub()).mult()).add()) 
                #print(t)
                #print((PointOp(c, nearestPoint).dist()))
                if PointOp(c, nearestPoint).distSq() < 13**2 and PointOp((PointOp(c, nearestPoint).dist()), self.getVelocity()).dot() >= 0: #and PointOp(PointOp(c, nearestPoint).dist(), target.getVelocity()).dot() <= 0:
                        d = self.getVelocity()
                        bma = PointOp(b,a).sub()
                        bmaDot = PointOp(bma,bma).dot()
                        vDotBma = PointOp(d,bma).dot()
                        
                        self.setVelocity(PointOp(PointOp((2*(vDotBma/bmaDot)),bma).mult(),self.getVelocity()).sub())
        
    
    def bounce(self,target):
		
        '''oldVS = self.getVelocity() #Old Velocity of self
        oldTV = target.getVelocity() #Old Velocity of target
        pS = self.getPosition() #Position of Self
        tP = target.getPosition()#Position of target
        xmx = PointOp(pS,tP).sub() #calculates the distance between the objects, or from self to target; you need to calculate target to self for calculating target's new velocity
        vmv = PointOp(oldVS,oldTV).sub() #calculates self - target velocities, need to do the opposite for target
        dvx = PointOp(vmv,xmx).dot() #calculates dot product of the velocities and the distance
        dxx = PointOp(xmx,xmx).dot() #calculates dot product of the distances
        div = dxx/dvx #calculates some number, needed to find new velocity
        newVS = PointOp(oldVS,PointOp(div,xmx).mult()).sub() #calculates self's new velocity'''

		#This should  work, sets the new velocities after collision. 
        d = [(target.getPosition()[0] - self.getPosition()[0]), (target.getPosition()[1] - self.getPosition()[1])]
        
        if PointOp(self.getPosition(), target.getPosition()).distSq() <= 16**2 and PointOp(d,self.getVelocity()).dot() >= 0 and PointOp(d, target.getVelocity()).dot() <= 0: #You will still need to detect if they are within 16 pixels of each other, though I don't know if you still need to check the dot products since we are no longer using the scalar.
            #print(target.getPosition(), self.getPosition())
            self.setVelocity( (PointOp(self.getVelocity(),PointOp((PointOp(PointOp(self.getVelocity(),target.getVelocity()).sub(),PointOp(self.getPosition(),target.getPosition()).sub()).dot()/PointOp(PointOp(self.getPosition(),target.getPosition()).sub(),PointOp(self.getPosition(),target.getPosition()).sub()).dot()),PointOp(self.getPosition(),target.getPosition()).sub()).mult()).sub()))
		
            target.setVelocity( (PointOp(target.getVelocity(),PointOp((PointOp(PointOp(target.getVelocity(),self.getVelocity()).sub(),PointOp(target.getPosition(),self.getPosition()).sub()).dot()/PointOp(PointOp(target.getPosition(),self.getPosition()).sub(),PointOp(target.getPosition(),self.getPosition()).sub()).dot()),PointOp(target.getPosition(),self.getPosition()).sub()).mult()).sub()))
		
		
class Stripes(Ball):
    
    def __init__(self, image, width, height, surface, velocity):
        super().__init__(self, image, width, height, surface, velocity)
        sripesScore = 0
    
    def Score(self):
        pocketList = [[409, 397],[17, 397],[406, 774],[406, 20],[20, 20],[20, 774]]
        for quard in pocketList:
            if PointOp(self.getPosition(), quard).distSq() < 8**2:
                stripesList.remove(self)
                stripesScore += 1

class Solids(Ball):
    
    def __init__(self, image, width, height, surface, velocity):
        super().__init__(self, image, width, height, surface, velocity)
        solidScore = 0
    
    def Score(self):
        pocketList = [[409, 397],[17, 397],[406, 774],[406, 20],[20, 20],[20, 774]]
        for quard in pocketList:
            if PointOp(self.getPosition(), quard).distSq() < 8**2:
                solidsList.remove(self)
                solidScore += 1

class Qball(Ball):
	
    def Score(self):
        pocketList = [[409, 397],[17, 397],[406, 774],[406, 20],[20, 20],[20, 774]]
        for quard in pocketList:
            if PointOp(self.getPosition(), quard).distSq() < 8**2:
                QList.remove(self)
    def Move(self):
        if self.getVelocity == [0,0]:
            return None
            #implement player movement
            # calculates distance from qball to mouse - that is our power
            # calculates slope of line frmo qball to mouse
        
def Pool(n):
	# Initialize PyGame and the drawing surface.
    pygame.init()
    width = 426
    height = 794
    surface = pygame.display.set_mode([width, height])
	# Initialize the background and balls.
    back = pygame.image.load("PoolImageOther.png")
    b = Background(back, surface)
    ballList = []
    imList = [[pygame.image.load("whiteball.bmp")],[pygame.image.load("9ball.bmp")],[pygame.image.load("7ball.bmp")],[pygame.image.load("12ball.bmp")],[pygame.image.load("15ball.bmp")],[pygame.image.load("8ball.bmp")],[pygame.image.load("1ball.bmp")],[pygame.image.load("6ball.bmp")],[pygame.image.load("10ball.bmp")],[pygame.image.load("3ball.bmp")],[pygame.image.load("14ball.bmp")],[pygame.image.load("11ball.bmp")],[pygame.image.load("2ball.bmp")],[pygame.image.load("13ball.bmp")],[pygame.image.load("4ball.bmp")],[pygame.image.load("5ball.bmp")]]
	
    posList = [[80,80],[213,213],[201.68,201.68],[224.32,201.68],[190.36,190.36],[213,190.36],[235.64,190.36],[179.04,179.04],[201.68,179.04],[224.32,179.04],[246.96,179.04],[167.72,167.72],[190.36,167.72],[213,167.72],[235.64,167.72],[258.28,167.72]]
    velList = [[-300,-300],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
	
    print(imList[0][0])
    for i in range(n):
        e = Ball(imList[i][0], 16, 16, surface, velList[i])
        e.setPosition(posList[i][0],posList[i][1])
        ballList += [e]
    
    '''while len(Qlist) <1:
        if pygame.mouse.get_pressed() == True
            #implement something that places a new Qball at  pygame.mouse.get_pos()
    '''
    
    
    #timing stuff
    oldTime = None
    newTime = None
    numTimeStepPerFrame = 15
    newTime = time.time()
    time.sleep(0.01)
    while True:
		# Handle the user quitting or pressing a key.
        oldTime = newTime
        newTime = time.time()
        timeStep = (newTime - oldTime)/numTimeStepPerFrame
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.unicode

        s = len(ballList)
        
        pointList = [[30,51],[17,36],[6,34],[4,20],[4,4],[20,4],[34,6],[39,20],[51,30],[375,30],[387,20],[392,6],[406,4],[422,2],[422,20],[420,34],[409,36],[396,51],[396,378],[409,381],[420,385],[425,397],[420,409],[409,413],[396,413],[396,743],[409,758],[420,760],[422,774],[422,790],[406,790],[392,788],[387,774],[375,764],[51,764],[39,774],[34,788],[20,790],[4,790],[4,774],[6,760],[17,758],[30,743],[30,416],[17,413],[6,409],[1,397],[6,385],[17,382],[30,378], [30,51]]
        for k in range(numTimeStepPerFrame):
            for i in range(0,s-1):
                for j in range(i+1, s):
                    ballList[i].bounce(ballList[j])
                
            for i in range(s):
                ballList[i].updatePos(timeStep, pointList)
		

        boundLines = []

        b.draw()
        #pygame.draw.polygon(surface, [0,0,0], pointList, 2)
        for i in range(n):
            ballList[i].draw()
        pygame.display.flip()

if __name__ == "__main__":
    Pool(2)
