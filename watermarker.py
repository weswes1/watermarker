from PIL import Image
import numpy as np
import math

im = Image.open("thickimage.jpg")
edited = np.array(im)
copy = edited

# Watermarker App





m = len(edited)-1           		 	# Number of Rows
n = len(edited[0])-1         		 	# Number of Columns
m = float(m)
n = float(n)


print("This image has {} rows and {} columns. ".format(m,n))

thickness = int(math.floor(n/16))		# Thickness of W 
rowtocol = float(m/n)					# Row to column ratio
slopeLine = (round(4*rowtocol))		# Line of slope joining the (0,m) pixel to the (0,n/4) pixel
print(slopeLine)





quarter_row=math.floor(m/4)
quarter_col=math.floor(n/4)




if slopeLine==0:
	print("0 slopeLine error. Corrupt image. This is a case that I must figure out. ")

else:

	for byfour in range(0,int(thickness)):
		for k in range(0,int(4*m)):          # We will transverse all of the rows.
			if (k <= m - 1):
				copy[k][byfour] = [255,255,255]
				if(k%slopeLine==0):
					byfour=byfour+1
		if (m<k<=2*k):
			for byfour in range(0,thickness):
				i = m
				j = quarter_col+byfour
				while ( i>=0 ):
						copy[i][j] = [0,0,0]
						if(i%slopeLine==0):
							j=j+1
						i=i-1
		if (2*m<k<= 3*k):
			for byfour in range(0,thickness):
				i = 0
				j = 2*quarter_col+byfour
				while ( i<=m ):
						copy[i][j] = [255,255,255]
						if(i%slopeLine==0):
							j=j+1
						i=i+1
		if (3*m<k<=4*m):
			for byfour in range(0,thickness):
				i = m
				j = 3*quarter_col+byfour
				while ( i>= 0 and j < n):
						copy[i][j] = [0,0,0]
						if(i%slopeLine==0):
							j=j+1
						i=i-1



Image.fromarray(copy).show()




