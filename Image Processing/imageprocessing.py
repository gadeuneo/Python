import math
import cImage



### LOADING AND DRAWING IMAGES ###

# x increases to the right and y increases down. That is, x = column, y = row.
# Each RGB channel is measured from 0 to 255.
# Implementation detail: An 'image window' is a pair [image, window].

def imageWindowFromFile(fileName):
	'''Given the name of an image file, returns an image window for it. You should have only one of these file-based image windows active in your program at any given time.'''
	image = cImage.FileImage(fileName)
	window = cImage.ImageWin(fileName, image.getWidth() + 16, image.getHeight())
	return [image, window]

def emptyImageWindow(imageWindow):
	'''Returns a new image window object, of the same size as the given one. The new image window draws into the same window as the original, but the memory for storing its image is separate from the memory for the original image.'''
	image = cImage.EmptyImage(imageWidth(imageWindow), imageHeight(imageWindow))
	return [image, imageWindow[1]]

def imageWidth(imageWindow):
	'''Given an image window, returns its width --- the number of columns. The window is slightly wider than the image.'''
	return imageWindow[0].getWidth()

def imageHeight(imageWindow):
	'''Given an image window, returns its height --- the number of rows.'''
	return imageWindow[0].getHeight()

def pixelRGB(imageWindow, x, y):
	'''Given an image window and an (x, y) point in that window, returns a list [r, g, b] for the color of the pixel at (x, y). The user must ensure that 0 <= x <= width and 0 <= y < height. Each RGB channel is measured from 0 to 255.'''
	pixel = imageWindow[0].getPixel(x, y)
	return [pixel.getRed(), pixel.getGreen(), pixel.getBlue()]

def setPixelRGB(imageWindow, x, y, rgb):
	'''Given an image window, an (x, y) point in that window, and a list [r, g, b] describing a color, sets the pixel at (x, y) to have that color. The user must ensure that 0 <= x <= width and 0 <= y < height. Each RGB channel is measured from 0 to 255. You have to call drawImage after this, to see the change.'''
	pixel = cImage.Pixel(rgb[0], rgb[1], rgb[2])
	imageWindow[0].setPixel(x, y, pixel)

def drawImage(imageWindow):
	'''Given an image window, draws the image in the window.'''
	imageWindow[0].draw(imageWindow[1])

def mouseXY(imageWindow):
	'''Given an image window, waits for the user to click the mouse in the window, and then returns the (x, y) coordinates of the click. Notice that an image window is slightly wider than the image that it holds. So x may be larger than the image width.'''
	xy = imageWindow[1].getMouse()
	return [xy[0] - 3, xy[1] - 3]

def saveFile(imageWindow, fileName, fileType):
	'''imageWindow is an image window. fileName is a string. fileType is a string such as "jpg".'''
	imageWindow[0].savePIL(fileName, fileType)

#def cleanUpImageWindow(imageWindow):
#	imageWindow[1].exitOnClick()



### CONVOLUTION ###

# k should be (2 r + 1) x (2 r + 1), where r is an integer.
# r is the radius of the kernel k.
def imageConvolved(imageWindow, k):
	newImageWindow = emptyImageWindow(imageWindow)
	r = (len(k) - 1) // 2
	for x in range(r, imageWidth(imageWindow) - r):
		for y in range(r, imageHeight(imageWindow) - r):
			newRGB = [0, 0, 0]
			# i is like x and j is like y, in the kernel.
			for i in range(len(k)):
				for j in range(len(k)):
					rgb = pixelRGB(imageWindow, x + i - r, y + j - r)
					newRGB[0] += k[j][i] * rgb[0]
					newRGB[1] += k[j][i] * rgb[1]
					newRGB[2] += k[j][i] * rgb[2]
			newRGB = list(map(lambda x: min(255, max(0, int(x))), newRGB))
			setPixelRGB(newImageWindow, x, y, newRGB)
	return newImageWindow

blurKernel3 = [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]

blurKernel5 = [[1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25]]

rakeKernel5 = [[0, 0, 1 / 5, 0, 0], [0, 0, 1 / 5, 0, 0], [0, 0, 1 / 5, 0, 0], [0, 0, 1 / 5, 0, 0], [0, 0, 1 / 5, 0, 0]]

def gaussianKernel(r, sigma):
	'''Returns a (2 r + 1) x (2 r + 1) kernel, approximating the two-dimensional normal distribution density with standard deviation sigma. The kernel is normalized to have total weight 1.'''
	# Build k unnormalized.
	k = []
	for y in range(-r, r + 1):
		row = []
		for x in range(-r, r + 1):
			unnormalized = math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
			row += [unnormalized]
		k += [row]
	# Normalize k to have total weight 1.
	total = sum(map(sum, k))
	for i in range(len(k)):
		for j in range(len(k)):
			k[i][j] /= total
	return k

sharpenKernel3 = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]






### THREADING ###

def imageThreaded(imageWindowA, imageWindowB, rgbFunc):
	newImageWindow = emptyImageWindow(imageWindowA)
	for x in range(imageWidth(imageWindowA)):
		for y in range(imageHeight(imageWindowA)):
			rgbA = pixelRGB(imageWindowA, x, y)
			rgbB = pixelRGB(imageWindowB, x, y)
			newRGB = rgbFunc(rgbA, rgbB)
			setPixelRGB(newImageWindow, x, y, newRGB)
	return newImageWindow

def averageRGB(rgbA, rgbB):
	return [(rgbA[0] + rgbB[0]) // 2, (rgbA[1] + rgbB[1]) // 2, (rgbA[2] + rgbB[2]) // 2]

def redRGB(rgb):
	return [rgb[0],0,0]
	
def noGreen(rgb):
	return [rgb[0],0,rgb[2]]
	
def GREEN(rgb):
	return [rgb[0], rgb[1]*2, rgb[2]]
	
def noRed(rgb):
	return [0,rgb[1],rgb[2]]


## MAPPING ##

def imageMapped(imageWindow, rgbFunc):
	newImageWindow = emptyImageWindow(imageWindow)
	for x in range(imageWidth(imageWindow)):
		for y in range(imageHeight(imageWindow)):
			rgb = pixelRGB(imageWindow, x, y)
			newRGB = rgbFunc(rgb)
			setPixelRGB(newImageWindow, x, y, newRGB)
	return newImageWindow	


## ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT ASSIGNMENT##	

##GREEN SCREEN##
def greenScreenRGB(rgbActor, rgbBackground):
	'''Given two RGB colors, returns one or the other, depending on whether the first one is "green".'''
	#[red,green,blue] [red<green>blue] green >= 82 to be considered "green"
	if rgbActor[1] < rgbActor[0] or rgbActor[1] < rgbActor[2] or rgbActor[1] < 82:
		return rgbActor
	else:
		return rgbBackground
	

def greenScreenedImage(actorImageWindow, backgroundImageWindow):
	'''Given two image windows (with images of the same size), returns a new image window, formed by green-screening the actor against the background.'''
	#Use greenScreenRGB function and imageThreaded in 2 lines of code
	return imageThreaded(actorImageWindow, backgroundImageWindow, greenScreenRGB)
	
##EDGE DETECTION##
 
redKernelHN = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
redKernelH = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

redKernelVN = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
redKernelV = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]

def blacktowhite(image):
	newImage=emptyImageWindow(image)
	for x in range(imageWidth(image)):
		for y in range (imageHeight(image)):
			rgb = pixelRGB(image,x,y)
			newRGB = []
			if rgb == [0,0,0]:
				newRGB = [255,255,255]
			else:
				newRGB = [0,0,0]
			setPixelRGB(newImage,x,y,newRGB)
	return newImage

def maxN(n,m):
	if (n[0]+n[1]+n[2])>(m[0]+m[1]+m[2]):
		return n
	else:
		return m
	
def maxRGB(rgbA, rgbB):
	return thread(maxN, rgbA, rgbB)

def edgeImage(imageWindow):
	'''Given an image window, returns a new image window capturing the edges in the original image.'''
	VertImage = imageConvolved(imageWindow, redKernelV)
	VertImageN = imageConvolved(imageWindow, redKernelVN)
	VImage = imageThreaded(VertImage, VertImageN, maxN)
	HorzImage = imageConvolved(imageWindow,	redKernelH)
	HorzImageN = imageConvolved(imageWindow, redKernelHN)
	HImage = imageThreaded(HorzImage, HorzImageN, maxN)
	return blacktowhite(imageThreaded(VImage, HImage, maxN))


##INKING##

def blackEdge(black, white):
	if black == [0,0,0]:
		return black
	else:
		return white

def blackSImage(black, white):
	return imageThreaded(black,white, blackEdge)		
		
def inkedImage(image):
	'''Given an image window, returns a new image window with the edges inked.'''
	newImage = blackSImage(edgeImage(image),image)
	return newImage


	
### USER CUSTOMIZATION ###

vertEdgeKernel3 = [
[-1, 0, 1], 
[-2, 0, 2], 
[-1, 0, 1]]

horizEdgeKernel3 = [
[1, 2, 1], 
[0, 0, 0], 
[-1, -2, -1]]

daigEdgeKernel3R = [
[0,1,2],
[-1,0,1],
[-1,-2,0]]

daigEdgeKernel3L = [
[2,1,0],
[1,0,-1],
[0,-2,-1]]

ansEdgeKernel = [
[-1, -2, 0], 
[-2, 0, 2], 
[0, 2, 1]]

def main():
	# Load, alter, and draw an image.
	#imageWindow = imageWindowFromFile("stephencolbert.jpg")
	#imageWindow2 = imageWindowFromFile("elcapitan.jpg")
	#imageWindow3 = imageWindowFromFile("small.gif")
	imageWindow4 = imageWindowFromFile("barackObama.jpg")
	imageWindow = imageConvolved(imageWindow4, ansEdgeKernel)
	#imageWindow = greenScreenedImage(imageWindow, imageWindow2) #Green screen code 
	#imageWindow = edgeImage(imageWindow3) #Edge Dectection Code
	#imageWindow = inkedImage(imageWindow3) #Ink Image Code
	#imageWindow = imageWindow3 #Test pixels
	drawImage(imageWindow)
	# Let the user sample pixels.
	xy = mouseXY(imageWindow)
	while 0 <= xy[0] < imageWidth(imageWindow) and 0 <= xy[1] < imageHeight(imageWindow):
		rgb = pixelRGB(imageWindow, xy[0], xy[1])
		print("pixel", xy[0], xy[1], "is", rgb)
		xy = mouseXY(imageWindow)
	#cleanUpImageWindow(imageWindow)



if __name__ == "__main__":
	main()



