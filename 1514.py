a,b=input().split()
c=len(a)
d=len(b)
if c>d:
    print(b,a)
elif c<d:
    print(a,b)
elif int(a)>int(b):
    print(b,a)
elif int(a)<int(b):
    print(a,b)
