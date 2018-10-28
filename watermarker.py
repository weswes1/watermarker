from PIL import Image
import numpy as np
import math

im = Image.open("owl.jpg")
edited = np.array(im)
copy = edited

# Watermarker App

m = len(edited)-1            # Number of rows
n = len(edited[0])-1         # Number of Columns

print("This image has {} rows and {} columns. ".format(m,n))
quarter_row=math.floor(m/4)
quarter_col=math.floor(n/4)

edited[276,69]=[255,255,255]
edited[66,279]=[255,255,255]




for k in range(1,4*m):          # We will transverse the number of rows 4 times. (Up and down 4 times, W)

	if (k <= m):    # First part of the W, this will take m iterations

		while()

		copy[i][j] = [255,255,255]

		if (j%4==0):
			j=j+1
		i=i+1
		print(i,j)

		#for z in range(0,2):
			#copy[i][j][z] = 255
			#(edited[i][j][z]+edited[i+1][j][z]+edited[i-1][j][z]+edited[i][j+1][z]+edited[i][j-1][z]+edited[i-1][j-1][z]+edited[i+1][j+1][z]+edited[i+1][j-1][z]+edited[i-1][j+1][z])/9
		


Image.fromarray(copy).show()

"""
	elif (quarter_col < k <= 2*quarter_col):			# Second part of the W, another m iterations

		i = m-1
		j = quarter_col

		while i > 0:
		# Decrease the number of rows, increase the number of columns 

			for z in range(0,2):
				print(i,j)
				copy[i][j][z] = (edited[i][j][z]+edited[i+1][j][z]+edited[i-1][j][z]+edited[i][j+1][z]+edited[i][j-1][z]+edited[i-1][j-1][z]+edited[i+1][j+1][z]+edited[i+1][j-1][z]+edited[i-1][j+1][z])/9

			i=i-1
			j=j+1



		
	elif (2*quarter_col < k <= 3*quarter_col):		# Third part of the W, "" "" iterations
		pass

	elif (3*quarter_col < k < n):						# Final part of the W, "" "" iterations
		pass

"""






def averageFilter(filepath):
	im = Image.open(filepath)
	edited = np.array(im)
	for index1 in range(1,m):
		for index2 in range(1,n):
			for i in range(0,2):
				copy[index1][index2][i] = (edited[index1][index2][i]+edited[index1+1][index2][i]+edited[index1-1][index2][i]+edited[index1][index2+1][i]+edited[index1][index2-1][i]+edited[index1-1][index2-1][i]+edited[index1+1][index2+1][i]+edited[index1+1][index2-1][i]+edited[index1-1][index2+1][i])/9







