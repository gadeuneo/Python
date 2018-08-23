from PIL import Image
import io


background = Image.open("carl cells.JPG")
overlay = Image.open("carl map.JPG")
other = Image.open("carl gyms.JPG")


background = background.convert("RGB")
overlay = overlay.convert("RGB")
other = other.convert("RGB")


background = background.resize((1000, 1000))
overlay = overlay.resize((1000, 1000))
other = other.resize((1000, 1000))


#for i in range(0,2):
'''
for x in range(0,100):
	for i in range(0,10):
		for j in range(0,10):
			img = Image.blend(background, overlay, i/10)
			new_img = Image.blend(img, other, j/10)
			#new_img.save("D:/james/Downloads/Pogo images/new%s.JPG"%x,"JPEG")


'''


   

file = open("testfile.txt","w") 
'''
for x in range(0,100):
	for i in range(0,10):
		for j in range(0,10):
			file.write("%s\n"%x)
			file.write("%s\n"%[i/10,j/10])


file.close() 
'''

f=[]

	
for i in range(0,10):
	for j in range(0,10):
		#print(x)
		#print([i/10,j/10])
		#file.write("%s\n"%x)
		#file.write("%s\n"%[i/10,j/10])
		f.append([i/10,j/10])

file.write(str(f))
file.close() 


for x in range(len(f)):
	img = Image.blend(background, overlay, f[x][0])
	new_img = Image.blend(img, other, f[x][1])
	new_img.save("D:/james/Downloads/Carleton/new%s.JPG"%x,"JPEG")
		
			
			
			
			
#




