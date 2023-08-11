k=int(input())
a=[[0]*19 for i in range(19)]
for i in range(k):
    x,y=map(int,input().split())
    a[x-1][y-1]=1
    

for i in a:
    for j in i:
        print(j,end=' ')
    print()
