a=int(input())
l=list()
for i in range(a):
    a,b=input().split()
    l.append([a,int(b)])
l.sort(key= lambda x:x[1],reverse=True)
print(l[2][0])
