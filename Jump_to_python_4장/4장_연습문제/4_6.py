# 6. 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해보자.
# 기존의 내용은 유지하면서 추가하는 방식을 사용할 것

# 나의 코드
# user_input = input("저장할 내용을 입력하세요.")
# f = open('test.txt', 'a')
# f.write(user_input)
# f.write('\n')
# f.close()

# test.txt 파일 확인 결과 "Life is too longI'm so tired."가 입력되어 있음
# 줄바꿈이 되지 않았음 ㅠㅠ 
# 정답을 확인해보니 똑같은데 왜 줄바꿈이 되지

# 나의 두 번재 시도
# user_input = input("저장할 내용을 입력하세요.")
# f = open('test.txt', 'a')
# f.write('\n')
# f.write(user_input)
# f.close()

# 출력값
# Life is terrible!!!Python is very fun
#
# 이렇게하면되겠지

# 줄바꿈 위치를 이동시켜주었다.
# 왜냐하면 test 파일에는 이미 앞의 연습문제로 입력된 값이 있었고
# 나는 그 뒤에 문장을 적는 거라 줄바꿈 후 입력 문장을 넣어주니 잘 실행되었음

# for문으로 해볼까?
user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')
for i in range(3):
    line = "---"
    f.write(line)
    f.write(user_input)
f.close()

# '될까?'를 입력했더니 ---될까?---될까?---될까? 가 출력되었다!
# 아직 뭔가 서투른 실력이지만 그냥 이것저것 시도해보았다!
