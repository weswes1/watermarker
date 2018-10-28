from PIL import Image
import numpy as np
import math

im = Image.open("owl.jpg")
arr = np.array(im)
edited = arr


# Make the image black

m = len(edited)
n = len(edited[0])

for i in range(0,m):
	for j in range(0,n):
		edited[i,j]=[0,0,0]

q1=int(math.floor(m/7))
q2=int(math.floor(n/7))

# Spell out my name in the image
# First part of the W
for i in range(0,q1):
	for j in range(0,q2):
		if (i==j):
			edited[i,j]=[255,255,255]

i=q1
j=q2

# Spell out the second part of the W
for k in range(0,q2):
	edited[i,j]=[255,255,255]
	i=i-1
	j=j+1

# Spell out the third part of the W. The starting position will be [0,2*q1]
for k in range(0,q2):
	edited[i,j]=[255,255,255]

	i=i+1
	j=j+1

i=q1
j=3*q2

# Spell out the fourth part of the W. The starting position will be [0,3*q1]
for k in range(0,q2):
	edited[i,j]=[255,255,255]
	i=i-1
	j=j+1


for k in range(0,q2):
	edited[k,4*q2+10]=[255,255,255]

for k in range(0,q2):
	edited[0,4*q2+10+k]=[255,255,255]
	edited[(math.floor(1.5*q2/3)),4*q2+10+k]=[255,255,255]
	edited[(q2),4*q2+10+k]=[255,255,255]

for k in range(0,q2):
	edited[3,m-3-k]=[255,255,255]
	edited[(math.floor(1.5*q2/3)),m-3-k]=[255,255,255]
	edited[q2,m-3-k]=[255,255,255]

for k in range(0,int(math.floor(q2/2))-2):
	edited[k+3,1+6*q1]=[255,255,255]

for k in range(0,int(math.floor(q2/2))):
	edited[math.floor(q2/2)+k+1,m-3]=[255,255,255]


Image.fromarray(edited).show()


'''
# Make the image white

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		edited[i,j]=[255,255,255]

# Make the image grey

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		edited[i,j]=[255,255,255]
white = Image.fromarray(edited)
# white.show()

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		edited[i,j]=[128,128,128]
gray = Image.fromarray(edited)
# gray.show()

for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		if (i%2==0):
			edited[i,j]=[0,0,0]
		else:
			edited[i,j]=[255,255,255]

striped = Image.fromarray(edited)
# striped.show()


for i in range(0,len(edited)):
	for j in range(0,len(edited[0])):
		if (i%2==0 and j%2==0):
			edited[i,j]=[0,0,0]
		else:
			edited[i,j]=[255,255,255]

dotted = Image.fromarray(edited)
# dotted.show()




# Trippy pattern, Diagnol iteration

m = len(edited) - 1    # Number of rows 
n = len(edited[0]) - 1 # Numbers of columns 

for k in range(0,m):
	if (k%2==0):	
		i=k
		j=0
		while (i >=0 ):
			edited[i,j]=[i,j,i^j]
			i = i - 1
			j = j+1

for k in range(0,n):
	if (k%2==0):
		i=m
		j=k
		while(j < n):
			edited[i,j]=[i,j,i^j]
			i=i-1
			j=j+1


for k in range(0,n):
	if (k%5==0):	
		i=k
		j=0
		while (i >=0 ):
			edited[i,j]=[i^j,j^i^j,i^j^k]
			i = i - 1
			j = j+1



# Let's try out an image blurring, where we map each pixel to the average of it's surrounding pixels.

for i in range(1,len(edited)):
	for j in range(1,len(edited[0])):
		edited[i,j]=[[edited[i+1][j]+edited[i-1][j]+edited[i][j+1]+edited[i][j-1]+edited[i+1][j+1]+edited[j-1][j-1]+edited[j+1][i-1]+edited[j-1][i+1],
		[edited[i+1][j]+edited[i-1][j]+edited[i][j+1]+edited[i][j-1]+edited[i+1][j+1]+edited[j-1][j-1]+edited[j+1][i-1]+edited[j-1][i+1],
		[edited[i+1][j]+edited[i-1][j]+edited[i][j+1]+edited[i][j-1]+edited[i+1][j+1]+edited[j-1][j-1]+edited[j+1][i-1]+edited[j-1][i+1]]

av = Image.fromarray(edited)
av.show()
'''






