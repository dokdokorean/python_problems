ch=input('문자 1개를 입력하시오:')
if len(ch)!=0:
    ch=ch[0]
    chv=ord(ch)
    print('문자:%s|t코드 값:%d[%s]'%(ch,chv,hex(chv)))
