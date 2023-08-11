b=int(input())
a=str(input())
l=list()
for i in a:
    l.append(i)
l.sort()
for i in l:
    print(i,end='')
