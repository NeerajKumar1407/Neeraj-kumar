"""Given a queue and an integer k. reverse first k elements. Return the upadated
queue. (Input: size=5, 12345, K=3)"""



list1 = input()
K = 3
list2 = []

for i in range(len(list1)):
    
   if i < K:
       list2.append(list1[i])
   if i == K:
       list2.reverse()
   if i >= K:
       list2.append(list1[i])
   
for item in list2:
    print(item,end=" ")
  
