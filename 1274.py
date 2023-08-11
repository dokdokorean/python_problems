import math
a=int(input())
for i in range(2,int(math.sqrt(a))+1):
    if a%i==0:
        print('not prime')
    elif a==1:
        print('not prime')
    elif a==2 or a==3:
        print('prime')
    
    elif a%i!=0:
        print('prime')
    
    

        
    
