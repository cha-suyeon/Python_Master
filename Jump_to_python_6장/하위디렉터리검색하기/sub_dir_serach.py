
import os 

def search(dirname):
    filenames = os.listdir(dirname) # os.listdir 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있음
    for filename in filenames:
        full_filename = os.path.join(dirname, filename) # 디렉터리를 포함한 전체 경로를 구하기 위해
        print(full_filename)

search("C:/")

