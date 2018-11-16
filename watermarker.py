														

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


col = 0
row = 0




print(im.shape())



if (m*n < 8):
	edited[m,n]=[255,255,255]
	print("small image")

else:
	
	rowtoCol = m/n									    		# Row to Column ratio
	slopeLine = (4*rowtoCol)
	inverseslopeLine = round(1/slopeLine)
																# Slope of the line
	quartercol = math.floor(n/4)										# A quarter of the total number of columns
	thickness = int(round(n/16))								# Thickness of the W

	meanPixel = np.mean(edited, axis=(0,1))

	slopeLine = round(slopeLine)
	inverseslopeLine = round(inverseslopeLine)
	m = int(m)
	n = int(n)


"""
	if (slopeLine == 0):
		while (row <= m):
			for k in range(0,thickness+1):
				edited[row][col+k]=[0,0,0]
				edited[m-row][col+quartercol+k-thickness/2]=[0,0,0]
				edited[m-row][col+3*quartercol-k]=[0,0,0]
				edited[row][col+2*quartercol-k+thickness/2]=[0,0,0]
			if (col%inverseslopeLine==0):
				row += 1
			col+=1

	else:
		for row in range(0,m+1):															# Transverse the total number of rows one time
			for k in range(0,thickness+1):
				print(m-row,col+3*quartercol-k)
				edited[row,col+k] = [100,120,10]												
				edited[row,col+2*quartercol-k+thickness/2] = meanPixel			    
				edited[m-row,col+quartercol+k-thickness/2] = meanPixel		
				edited[m-row,col+3*quartercol-k] = [100,120,10] 								
			if (row % slopeLine == 0):
				col+=1

	edited[0,0]=[250,250,250]

	Image.fromarray(edited).show()

"""