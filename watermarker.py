from PIL import Image
import numpy as np
import math

im = Image.open("owl.jpg")
edited = np.array(im)
copy = edited

# Watermarker App

m = len(edited)-1            # Number of rows
n = len(edited[0])-1         # Number of Columns

thickness = int(math.floor(n/4))


# print("This image has {} rows and {} columns. ".format(m,n))

quarter_row=math.floor(m/4)
quarter_col=math.floor(n/4)





for byfour in range(1,thickness):

	for k in range(1,4*m):          # We will transverse all of the rows.

		# print("k is {} byfour is {}".format(k,byfour))

		if (k <= m - 1):

			for z in range(0,3):
				x = (float(edited[k][byfour][z])+float(edited[k+1][byfour][z])+float(edited[k-1][byfour][z])+float(edited[k][byfour+1][z])+float(edited[k][byfour-1][z])+float(edited[k-1][byfour-1][z])+float(edited[k+1][byfour+1][z])+float(edited[k+1][byfour-1][z])+float(edited[k-1][byfour+1][z]))/9
				x = math.floor(x)
				copy[k][byfour][z] = x

			if(k%4==0):
				byfour=byfour+1


#print(edited[1][1],edited[2][1],edited[0][1],edited[1][2],edited[1][0],edited[0][0],edited[2][2],edited[2][0],edited[0][2])
print(edited[1][1])
print((float(edited[1][1][0])+float(edited[2][1][0])+float(edited[0][1][0])+float(edited[1][2][0])+float(edited[1][0][0])+float(edited[0][0][0])+float(edited[2][2][0])+float(edited[2][0][0])+float(edited[0][2][0]))/9)
print((float(edited[1][1][1])+float(edited[2][1][1])+float(edited[0][1][1])+float(edited[1][2][1])+float(edited[1][0][1])+float(edited[0][0][1])+float(edited[2][2][1])+float(edited[2][0][1])+float(edited[0][2][1]))/9)
print((float(edited[1][1][2])+float(edited[2][1][2])+float(edited[0][1][2])+float(edited[1][2][2])+float(edited[1][0][2])+float(edited[0][0][2])+float(edited[2][2][2])+float(edited[2][0][2])+float(edited[0][2][2]))/9)


Image.fromarray(copy).show()



"""
	if (m<k<=2*k):
		i = m
		j = quarter_col
		
		while ( i>=0 ):
				copy[i][j] = [255,255,255]
				if(i%4==0):
					j=j+1
				i=i-1


	if (2*m < k <= 3*k):
		i = 0
		j = 2*quarter_col
		while ( i<=m ):
				copy[i][j] = [255,255,255]

				if(i%4==0):
					j=j+1

				i=i+1


	if (3*m < k <= 4*m):
		i = m
		j = 3*quarter_col

		while ( i>= 0 ):
				copy[i][j] = [255,255,255]

				if(i%4==0):
					j=j+1
				i=i-1

		"""







