import os
newfolder=input('새로 생성할 데렉터리 이름을 입력하세요:')
try:
    os.mkdir(newfolder)
    print('[%s] 디렉터리르 생성했습니다.'%newfodler)
except Exception as e:
    print(e)
