from PIL import Image
import numpy as np
import math

im = Image.open("owl.jpg")
print("Welcome to the watermark picture editor")
arr = np.array(im)
edited = arr
print("Our image is {} rows {} columns and has a depth of {}, corresponding to the RGB values of each pixel in the image".format(len(arr),len(arr[0]),len(arr[0][1])))

'''
# Make the image black

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		edited[i,j]=[0,0,0]

black = Image.fromarray(edited)
# black.show()

# Make the image white

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		edited[i,j]=[255,255,255]

# Make the image grey

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		edited[i,j]=[255,255,255]
white = Image.fromarray(edited)
# white.show()

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		edited[i,j]=[128,128,128]
gray = Image.fromarray(edited)
# gray.show()

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		if (i%2==0):
			edited[i,j]=[0,0,0]
		else:
			edited[i,j]=[255,255,255]

striped = Image.fromarray(edited)
# striped.show()


for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		if (i%2==0 and j%2==0):
			edited[i,j]=[0,0,0]
		else:
			edited[i,j]=[255,255,255]

dotted = Image.fromarray(edited)
# dotted.show()

'''


# Trippy pattern, Diagnol iteration

m = len(edited) - 1    # Number of rows 
n = len(edited[0]) - 1 # Numbers of columns 

for k in range(0,m):
	if (k%2==0):	
		i=k
		j=0
		while (i >=0 ):
			edited[i,j]=[i,j,i^j]
			i = i - 1
			j = j+1

for k in range(0,n):
	if (k%2==0):
		i=m
		j=k
		while(j < n):
			edited[i,j]=[i,j,i^j]
			i=i-1
			j=j+1


for k in range(0,n):
	if (k%5==0):	
		i=k
		j=0
		while (i >=0 ):
			edited[i,j]=[i^j,j^i^j,i^j^k]
			i = i - 1
			j = j+1


black = Image.fromarray(edited)
black.show()


black = Image.fromarray(edited)
black.show()






