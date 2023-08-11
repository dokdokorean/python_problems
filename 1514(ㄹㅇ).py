l=[[0]*7 for i in range(7)]
chk=[]
for i in range(3):
    a,b=map(int,input().split())
    l[a-1][b-1]=2
def line(x,p):
    if p==0:
        for i in range(7):
            if [x,i] not in chk:
                if l[x][i]==2:
                    chk.append([x,i])
                    line(i,1)
                else:
                    l[3][i]=1
    else:
        for i in range(7):
            if [x,i] not in chk:
                if l[i][x]==2:
                    chk.append([i,x])
                    line(i,0)
                else:
                    l[i][x]=1
line(3,0)
for i in l:
    for j in i:
        print(j,end=' ')
    print()
