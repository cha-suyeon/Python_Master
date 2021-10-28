# 여기서 그 하위 디렉터리에서도 모든 파이썬 파일을 검색하는 것으로 만들어보자.

import os 

def search(dirname):
    try:
        filenames = os.listdir(dirname) # os.listdir 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있음
        for filename in filenames:
            full_filename = os.path.join(dirname, filename) # 디렉터리를 포함한 전체 경로를 구하기 위해
            if os.path.isdir(full_filename): # dir가 맞는지 확인하기 위한 함수
                search(full_filename) # dir일 경우 해당 경로를 입력 받고 search 함수 호출
            else:
                ext = os.path.splitext(full_filename)[-1] # 파일 이름에서 확장자만 추출하기 위한 함수
                # 파일 이름을 확장자 기준으로 두 부분으로 나누어줌.
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("C:/")




