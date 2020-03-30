"""You are given an integer n and you have to print F(n)th term of the sequence
if F(n)=(1)+(2*3)+(4*5*6)+...n. (Input:3)"""


n=int(input())
a=1
sum=0
for i in range(1,n+1):
	mul=1
	for j in range(i):
		mul=mul*a
		a=a+1
	sum=sum+mul
print(sum)
