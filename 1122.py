a=input()
a=int(a)
b=a//60
c=a%60
if a-60<0:
    print(0,a)
elif a-60>=0:
    print(b,c)
