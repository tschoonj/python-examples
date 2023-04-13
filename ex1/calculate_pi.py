from random import random

N=10000000
n2=0
for i in range(N):
   x=random()
   y=random()
   #print(f'{x=}')
   #print(f'{y=}')
   sidesum = x**2+y**2
   if sidesum<1:
      n2 = n2+1

temp=((n2/N)*4)
print(temp) 
   