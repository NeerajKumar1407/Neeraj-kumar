"""Print the following pattern for given number of rows. (Input: 5)"""


x = int(input())
for a in range(x):
	c=1
	d=0
	for b in range(1,2*x+1):
		d+=1
		if c+a <x+1:
			print(c,end="")
		else:
			print("*",end="")
		if d<x:
			c+=1
		elif d==x:
			c=c
		else:
			c-=1
	print()
