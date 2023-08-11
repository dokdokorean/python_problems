n=int(input())
l=[]
c=1
for i in range(n):
    a=[]
    for j in range(n):
        a.append(c)
        c+=1
    if i%2==0:
        a.reverse()
    l.append(a)
for i in l:
    for j in i:
        print(j,end=' ')
    print()
        
