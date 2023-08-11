import sys
a=list(map(int,input().split()))
b=0
for i in a:
                if i%5==0:
                                b+=1
                                print(i)
                                sys.exit()
if b==0:
                print('0')

