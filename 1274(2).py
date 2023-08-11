import math
a=int(input())
b=True
for i in range(2,int(math.sqrt(a))+1):
    if a%i==0:
        b=False
        break
if b:
    print('prime')
else:
    print('not prime')
