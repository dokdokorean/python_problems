a=int(input())
l=input().split()
for i in range(a):
      k=l[i:]+l[0:i]
      for j in k:
          print(j,end=' ')
      print()
           
      
      
