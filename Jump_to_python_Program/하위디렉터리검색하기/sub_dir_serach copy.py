# 여기서 확장자가 '.py'인 것만 찾기 -> *.py

import os 

def search(dirname):
    filenames = os.listdir(dirname) # os.listdir 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있음
    for filename in filenames:
        full_filename = os.path.join(dirname, filename) # 디렉터리를 포함한 전체 경로를 구하기 위해
        ext = os.path.splitext(full_filename)[-1] # 파일 이름에서 확장자만 추출하기 위한 함수
        # 파일 이름을 확장자 기준으로 두 부분으로 나누어줌.
        if ext == '.py':
            print(full_filename)

search("C:/")
# .py가 없다면 아무 것도 출력되지 않음


