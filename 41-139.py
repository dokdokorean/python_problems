f=open('stockcode.txt','r')
lines=f.readlines()
for line_num,line in enimerate(lines):
    print('%d %s'%(line_num+1,line),end='')
    f.close()
