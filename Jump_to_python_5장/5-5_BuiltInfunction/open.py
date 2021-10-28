# open(filename, [mode]), 파일 이름과 읽기 방법을 입력받아 파일 객체를 돌려주는 함수
# 읽기 방법 mode를 생략하면 기본값인 읽기 전용 모드(r)로 패일 객체를 만들어 돌려준다.

# w: 쓰기 모드/ r: 읽기 모드/ a: 추가 모드/ b: 바이너리 모드
# b는 wra와 함께 사용됨

f = open("binary_file", "rb") # 바이너리 읽기 모드

fread = open("read_mode.txt", 'r')
fread2 = open("read_mode.txt")
# fread, fread2는 동일한 방법이다.

fappend = open("append_mode.txt", 'a')
# 추가 모드(a)로 파일을 여는 예시
