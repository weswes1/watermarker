														

															# Watermarker App
															# Import modules

from PIL import Image
import numpy as np
import math


															# Open the image and store it as a numpy array, make a copy of the image


im = Image.open("thinimage.jpg")
edited = np.array(im)
copy = edited

													
m = float(len(edited)-1)       		 						# Number of Rows
n = float(len(edited[0])-1)     		 					# Number of Columns

rowtoCol = float(m/n)									    # Row to Column ratio
coltoRow = (float(n/m))										# Column to row ratio

slopeLine = round(4*rowtoCol)								# Slope of the line
quartercol = round(n/4)										# A quarter of the total number of columns
thickness = round(n/16)										# Thickness of the W

meanPixel = np.mean(edited, axis=(0,1))


print(coltoRow)
print("Number of rows: {} number of columns: {} Row to Column ratio: {} Column to Row ratio: {} slopeLine: {}".format(m,n,rowtoCol,coltoRow,slopeLine))

col = 0
row = 0


# 101 rows, and 344 columns

print((round(coltoRow/4)))

if (slopeLine == 0):
	while (row <= m):
		for k in range(0,int(thickness)+1):
			edited[row][col+k]=[0,0,0]
			edited[m-row][col+quartercol+k-round(thickness/2)]=[0,0,0]
			edited[m-row][col+3*quartercol-k]=[0,0,0]
			edited[row][col+2*quartercol-k+round(thickness/2)]=[0,0,0]

		if (col%(round(coltoRow/4))==0):
			row += 1

		col+=1




else:
	for row in range(0,int(m)):															# Transverse the total number of rows one time
		for k in range(0,int(thickness)+1):
			edited[row,col+k] = meanPixel												
			edited[row,col+2*quartercol-k+round(thickness/2)] = meanPixel			    
			edited[m-row,col+quartercol+k-round(thickness/2)] = meanPixel   			
			edited[m-row,col+3*quartercol-k] = meanPixel 								
		if (row % slopeLine == 0):
			col+=1



Image.fromarray(edited).show()

