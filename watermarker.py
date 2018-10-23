from PIL import Image
import numpy as np

im = Image.open("owl.jpg")
print("Welcome to the watermark picture editor")
arr = np.array(im)
edited = arr
print("Our image is {} rows {} columns and has a depth of {}, corresponding to the RGB values of each pixel in the image".format(len(arr),len(arr[0]),len(arr[0][1])))


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


# Diagnol lines

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		for k in range(0,127):
				edited[0,2*k]=[255,255,255]


black = Image.fromarray(edited)
black.show()





