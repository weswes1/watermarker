from PIL import Image
import numpy as np
import math

im = Image.open("test.jpg")
edited = np.array(im)
copy = edited

# Watermarker App

m = len(edited)-1            # Number of rows
n = len(edited[0])-1         # Number of Columns

thickness = int(math.floor(n/16))


print("This image has {} rows and {} columns. ".format(m,n))

quarter_row=math.floor(m/4)
quarter_col=math.floor(n/4)



for byfour in range(1,thickness):
	for k in range(0,4*m):          # We will transverse all of the rows.

		# print("k is {} byfour is {}".format(k,byfour))

		if (k <= m - 1):
			copy[k][byfour] = [255,255,255]

			if(k%4==0):
				byfour=byfour+1


	if (m<k<=2*k):
		for byfour in range(1,thickness):
			i = m
			j = quarter_col+byfour
			
			while ( i>=0 ):

					copy[i][j] = [0,0,0]

					if(i%4==0):
						j=j+1

					i=i-1

	if (2*m < k <= 3*k):

		for byfour in range(1,thickness):
			i = 0
			j = 2*quarter_col+byfour
			while ( i<=m ):
					copy[i][j] = [255,255,255]
					if(i%4==0):
						j=j+1

					i=i+1


	if (3*m < k <= 4*m):
		for byfour in range(1,thickness):
			i = m
			j = 3*quarter_col+byfour

			while ( i>= 0 and j < n):

					copy[i][j] = [0,0,0]

					if(i%4==0):
						j=j+1

					i=i-1





Image.fromarray(copy).show()




