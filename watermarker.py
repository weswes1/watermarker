														

															# Watermarker App
															# Import modules

from PIL import Image
import numpy as np
import skimage
from skimage import filters, img_as_ubyte
from matplotlib import pyplot as plt
import math


															# Open the image and store it as a numpy array, make a copy of the image


im = Image.open("owl.jpg")
edited = np.array(im)
copy = edited

													
m = float(len(edited)-1)       		 						# Number of Rows
n = float(len(edited[0])-1)     		 					# Number of Columns


gaussianBlur = skimage.filters.gaussian(copy,sigma=4)

gaussianBlur = img_as_ubyte(gaussianBlur)


col = 0
row = 0




if (m*n < 8):
	edited[m,n]=[255,255,255]

else:
	
	rowtoCol = m/n									    	# Row to Column ratio
	slopeLine = (4*rowtoCol)
	inverseslopeLine = round(1/slopeLine)					# Slope of the line
	quartercol = int(math.floor(n/4))						# A quarter of the total number of columns
	thickness = int(round(n/16))							# Thickness of the W
	meanPixel = np.mean(edited, axis=(0,1))
	slopeLine = round(slopeLine)
	inverseslopeLine = round(inverseslopeLine)
	m = int(m)
	n = int(n)
	if (slopeLine == 0):
		while (row <= m):
			for k in range(0,thickness+1):
				edited[row][col+k]=gaussianBlur[row][col+k]
				edited[m-row][col+quartercol+k-round(thickness/2)]=gaussianBlur[m-row][col+quartercol+k-round(thickness/2)]
				edited[m-row][col+3*quartercol-k]=gaussianBlur[m-row][col+3*quartercol-k]
				edited[row][col+2*quartercol-k+round(thickness/2)]= gaussianBlur[row][col+2*quartercol-k+round(thickness/2)]
			if (col%inverseslopeLine==0):
				row += 1
			col+=1
	else:
		for row in range(0,m+1):															# Transverse the total number of rows one time
			for k in range(0,thickness+1):
				edited[row,col+k] = gaussianBlur[row,col+k]											
				edited[row,col+2*quartercol-k+int(round(thickness/2))] = gaussianBlur[row,col+2*quartercol-k+int(round(thickness/2))]		    
				edited[m-row,col+quartercol+k-int(round(thickness/2))] = gaussianBlur[m-row,col+quartercol+k-int(round(thickness/2))]		
				edited[m-row,col+3*quartercol-k] = gaussianBlur[m-row,col+3*quartercol-k]				
			if (row % slopeLine == 0):
				col+=1




	# img = Image.fromarray(edited)
	# img.save('blurry.png')
	# img.show()
	# Image.fromarray(gaussianBlur).show()

plt.imshow(edited, interpolation='nearest')
plt.show()

