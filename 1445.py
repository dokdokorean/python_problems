a,b=int(input().split())
l=list()
for i in range(a):
    c=str(input())
    l.append(c)
for j in range(b):
    d=str(input())
    l.append(d)
l.sort()
for i in l:
    print(i,end=' ')

          
