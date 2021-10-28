# 5. 다음은 "test.txt" 이라는 파일에 "Life is too long" 문자열을 저장한 후
# 다시 그 파일을 읽어서 출력하는 프로그램이다.

# 문제에서 제시한 코드
# f1 = open("test.txt", "w")
# f1.write("Life is too long")

# f2 = open("test.txt", "r")
# print(f2.read())

# 이 프로그램은 우리가 예상한 "Life is too long"을 출력하지 않는다.
# 예상한 값을 출력할 수 있도록 수정해보자.

# 나의 코드 - 고치지 못함😂
# 정답 코드 👇

# f1 = open("test.txt", "w")
# f1.write("Life is too long")
# f1. close()
# f2 = open("test.txt", "r")
# print(f2.read())
# f2.close()

# 이 문제에서 제시한 오류는 파일의 close 개념이었다.
# 파일을 close 하지 않은 상태에서 다시 열면 파일에 저장한 데이터를 읽을 수 없다.
# 따라서 열린 파일 객체를 close로 닫아준 후 열어서 파일의 내용을 읽어야 함

# 안 보고 작성 해보기

f1 = open("test.txt", "w")
f1.write("Life is too boring")
f1.close()

f2 = open("test.txt", "r")
print(f2.read())
f2.close()

# with을 사용해서 해보기

with open("test.txt", "w") as f1:
    f1.write("Life is terrible!!!")
with open("test.txt", 'r') as f2:
    print(f2.read())