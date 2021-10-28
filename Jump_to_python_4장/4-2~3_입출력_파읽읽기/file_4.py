# 파일을 쓰기 모드로 열어 출력값 적는 다른 방법

f = open("C:/Users/chasu/OneDrive/바탕 화면/doit/새파일2.txt", "w")
for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    print(data)
f.close()

# 두 파일의 다른 점은 data를 출력하는 방법이었다.
# 두 번째 방법은 모니터에 출력하는 방법이었고
# 첫 번째 방법은 모니터 화면 대신 파일에 결괏값을 적는 방법이다.
# 두 방법의 차이점은 print 대신 파일 객체 f의 write 함수를 사용한 것 말고는 없다.

# f.write(data)
# print(data)