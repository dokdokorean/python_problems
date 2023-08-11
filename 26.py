import os
target_folder='tmp'
k=input('[%s]디렉터리를 삭제하시습니까?(y/n)'%target_folder)
if k=='y':
    try:
        os.rmdir(taget_folder)
        print('[%s]디렉터리를 삭제했습니다.'%target_folder)
    except Exception as e:
        print(e)
