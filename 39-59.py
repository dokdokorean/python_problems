import time
count=1
try:
    while True:
        print(count)
        count+=1
        time.sleep(3)
except KeyboardInterrupt:
    print('사용자에의해 프로그램이 중단되었습니다.')
