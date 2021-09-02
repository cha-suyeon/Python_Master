# readline 함수로 모든 내용을 읽어보기

f = open("C:/Users/chasu/OneDrive/바탕 화면/doit/새파일.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# while True: 무한 루프 안에서 f.readline()을 사용해 파일을 계속해서 한 줄씩 읽어 들인다.
# 만약 더 읽을 줄이 없으면 break를 수행한다.
# readline은 더 읽을 줄이 없다면 None을 출력한다.
