x=[1,2]
y=[3,2]
c= 2
def dot(x,y):
	total = 0
	for i in range(len(x)):
		total = total + x[i] * y[i]
	return total
	
#print(dot(x,y))

def sub(x,y):
	total = []
	for i in range(len(y)):
		total += [x[i] - y[i]]
	return total

#print(sub(x,y))

def mult(c,y):
	total = []
	for i in range(len(y)):
		total += [c*y[i]]
	return total
	
#print(mult(c,y))

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
	def setPosition(self,x,y):
		x = max(0,min(self.surface.get_width(),x))
		y = max(0,min(self.surface.get_height(), y)
		self.xy = [x,y]
		
	def bounce(self,target):
		'''
		oldVS = self.getVelocity #Old Velocity of self
		oldTV = target.getVelocity #Old Velocity of target
		pS = self.getPosition #Position of Self
		tP = target.getPosition #Position of target
		xmx = sub(pS,tP) #calculates the distance between the objects, or from self to target; you need to calculate target to self for calculating target's new velocity
		vmv = sub(oldVS,oldTV) #calculates self - target velocities, need to do the opposite for target
		dvx = dot(vmv,xmx) #calculates dot product of the velocities and the distance
		dxx = dot(xmx,xmx) #calculates dot product of the distances
		div = dxx/dvx #calculates some number, needed to find new velocity
		newVS = sub(oldVS,mult(div,xmx)) #calculates self's new velocity
		'''
		#This should  work, sets the new velocities after collision. 
		#You will still need to detect if they are within 16 pixels of each other, though I don't know if you still need to check the dot products since we are no longer using the scalar.
		self.setVelocity = (sub(self.getVelocity,mult((dot(sub(self.getVelocity,target.getVelocity),sub(self.getPosition,target.getPosition))/dot(sub(self.getPosition,target.getPosition),sub(self.getPosition,target.getPosition))),sub(self.getPosition,target.getPosition))))
		
		target.setVelocity = (sub(target.getVelocity,mult((dot(sub(target.getVelocity,self.getVelocity),sub(target.getPosition,self.getPosition))/dot(sub(target.getPosition,self.getPosition),sub(target.getPosition,self.getPosition))),sub(target.getPosition,self.getPosition))))
		
		
		