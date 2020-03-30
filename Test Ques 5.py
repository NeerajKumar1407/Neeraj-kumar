"""Given various subsequences of an array.print overall array:
Example: [1,3,5],[1,3,9],[9,5]
Array: [1,3,9,5]"""


import itertools
a=[[1,3,5],[1,3,9],[9,5]]
merged=list(itertools.chain(*a))
print(merged)
t=list(set(merged))
t.sort()
fin=[int(i) for i in t]
print(fin)
