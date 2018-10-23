from PIL import Image
import numpy as np

im = Image.open("owl.jpg")
print("Welcome to the watermark picture editor")
arr = np.array(im)
edited = arr
print("Our image is {} rows {} columns and has a depth of {}, corresponding to the RGB values of each pixel in the image".format(len(arr),len(arr[0]),len(arr[0][1])))


# Make the image white

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		edited[i,j]=[0,0,0]


