a, b = input().split()
a = int(a)
b= int(b)
c=0
for i in range(a, b + 1):
    if(i % 3== 0):
        c+=i
print(c)
        
