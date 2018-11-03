from PIL import Image
import numpy as np
import math
														# Watermarker App

copy = np.array(Image.open("owl.jpg"),dtype='int64')



m = float(len(copy)-1)     		 	# Number of Rows
n = float(len(copy[0])-1)        		# Number of Columns



copy[m,n]=[255,255,255]

# print("This image has {} rows and {} columns. ".format(m,n))

thickness = round(n/16)		# Thickness of W 
rowtocol = round(float(m/n))		# Row to column ratio
# print(rowtocol)
slopeLine = round(4*rowtocol)			# Line of slope joining the (0,m) pixel to the (0,n/4) pixel
# print(slopeLine)

quarter_row=math.floor(m/4)
quarter_col=math.floor(n/4)




for k in range(0,int(4*m)):			# We will traverse the total number of rows four times
	if (k < m):						# First section of the W
		for byfour in range(0,int(thickness)):  # Controls the wide of the W by starting a new 1-pixel wide diagnal line adjacent to the previous, thickness number of times 
			i=1
			j=byfour

			while (i < m):
				for z in range(0,2):
					copy[i][j][z] = (copy[i][j][z]+copy[i+1][j][z]+copy[i-1][j][z]+copy[i][j+1][z]+copy[i][j-1][z]+copy[i-1][j-1][z]+copy[i+1][j+1][z]+copy[i+1][j-1][z]+copy[i-1][j+1][z])/9
				if(i%slopeLine==0):
					j=j+1
				i=i+1

	if (m < k <= 2*k):					# Second section of the W 

		for byfour in range(0,int(thickness)):
			i = m-1
			j = quarter_col+byfour

			while (0 < i < m):
				for z in range(0,2):
					copy[i][j][z] = (copy[i][j][z]+copy[i+1][j][z]+copy[i-1][j][z]+copy[i][j+1][z]+copy[i][j-1][z]+copy[i-1][j-1][z]+copy[i+1][j+1][z]+copy[i+1][j-1][z]+copy[i-1][j+1][z])/9
				if(i%slopeLine==0):
					j=j+1
				i=i-1

	if (2*m < k <= 3*k):				# Third section of the W

		for byfour in range(0,int(thickness)):
			i = 1
			j = 2*quarter_col+byfour
			while ( i < m ):
				for z in range(0,2):
					copy[i][j][z] = (copy[i][j][z]+copy[i+1][j][z]+copy[i-1][j][z]+copy[i][j+1][z]+copy[i][j-1][z]+copy[i-1][j-1][z]+copy[i+1][j+1][z]+copy[i+1][j-1][z]+copy[i-1][j+1][z])/9
				if(i%slopeLine==0):
					j=j+1
				i=i+1


	if (3*m < k < 4*m):

		for byfour in range(0,int(thickness)):
			i = m-1
			j = 3*quarter_col+byfour
			while ( i > 0 and j < n):
				for z in range(0,2):
						copy[i][j][z] = (copy[i][j][z]+copy[i+1][j][z]+copy[i-1][j][z]+copy[i][j+1][z]+copy[i][j-1][z]+copy[i-1][j-1][z]+copy[i+1][j+1][z]+copy[i+1][j-1][z]+copy[i-1][j+1][z])/9
				if(i%slopeLine==0):
					j=j+1
				i=i-1



Image.fromarray(copy).show()




