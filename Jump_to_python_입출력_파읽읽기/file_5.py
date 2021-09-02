# 프로그램 외부에 저장된 파일을 읽는 여러 가지 방법
# readline 함수 사용하기

f = open("C:/Users/chasu/OneDrive/바탕 화면/doit/새파일.txt", "r")
line = f.readline()
print(line)
f.close()

# 1번째 줄입니다. 라는 결괏값이 출력된다.
# 위의 예는 f.open("새파일.txt", "r")로 파일을 읽기 모드로 연 후
# readline()을 사용해 파일의 첫 번째 줄을 읽어 출력하는 경우이다.
