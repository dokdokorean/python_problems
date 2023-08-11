expr1='2+3'
expr2='round(3,7)'
ret1=eval(expr1)
ret2=eval(expr2)
print('<%s>를eval()로 설저한 결과:'%expr1,end='');print(ret1)
print('<%s>를eval()로 설저한 결과:'%expr2,end='');print(ret2)
