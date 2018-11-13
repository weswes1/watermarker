														

															# Watermarker App

															# Import modules

from PIL import Image
import numpy as np
import math

															# Open the image and store it as a numpy array, make a copy of the image
im = Image.open("owl.jpg")
edited = np.array(im)
copy = edited

													
m = float(len(edited)-1)       		 						# Number of Rows
n = float(len(edited[0])-1)     		 					# Number of Columns
rowtoCol = round(m/n)									    # Row to Column ratio
slopeLine = 4*rowtoCol										# Slope of the line
quartercol = round(n/4)										# A quarter of the total number of columns
thickness = round(n/16)										# Thickness of the W


print("Number of rows: {} number of columns: {} Row to Column ratio: {} slopeLine: {}".format(m,n,rowtoCol,slopeLine))


col = 0

for row in range(0,int(m)):															# Transverse the total number of rows one time
	for k in range(0,int(thickness)):

		for rgbVAL in range(0,2):
			edited[row][col+k][rgbVAL] = float((int(copy[row][col+k][rgbVAL])+int(copy[row-1][col+k][rgbVAL])+int(copy[row+1][col+k][rgbVAL])+int(copy[row][col+k+1][rgbVAL])+int(copy[row][col+k-1][rgbVAL])+int(copy[row-1][col+k-1][rgbVAL])+int(copy[row+1][col+k+1][rgbVAL])+int(copy[row+1][col+k-1][rgbVAL])+int(copy[row-1][col+k+1][rgbVAL]))*(1/9))		# Yellow

			#edited[row,col+2*quartercol-k+round(thickness/2)][rgbVAL]=[255,255,255] 			# White

			#edited[m-row,col+quartercol+k-round(thickness/2)][rgbVAL]=[0,0,100]   				# Blue

			#edited[m-row,col+3*quartercol-k][rgbVAL]=[100,100,100] 							# Grey


	if (row % slopeLine == 0):
		col+=1


	

	


Image.fromarray(edited).show()

