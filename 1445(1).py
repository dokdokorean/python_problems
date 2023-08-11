a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=c+d
e.sort()
for i in e:
    print(i,end=' ')
