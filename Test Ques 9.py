"""Given k, find the geometric sum i.e 1 + 1/2 + 1/4 + 1/8 +...+1/(2^k)
using recursion. Return the answer.  (Input; 3)"""



n= int(input())
r= 0
for i in range(0,n+1):
    r+=(1/2**i)
print(r)
