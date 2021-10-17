# 6번과 다른 점
# readlines 함수 사용하기
# readline과 readlines

f = open("C:/Users/chasu/OneDrive/바탕 화면/Python_Master/새파일.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

print(lines)
# readlines 함수는 파일의 모든 줄을 읽어 각각의 줄을 요소로 갖는 리스트로 돌려준다.
# 따라서 위에서 lines는 리스트가 된다.
