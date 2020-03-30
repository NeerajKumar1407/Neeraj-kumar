"""Write a recursive function that returns the sum of the digits of a given
integer. (Imput: 12345)"""


def getSum(n): 
    sum = 0
    while (n != 0): 
      
        sum = sum + int(n % 10) 
        n = int(n/10) 
      
    return sum
  
n = 12345
print(getSum(n))

