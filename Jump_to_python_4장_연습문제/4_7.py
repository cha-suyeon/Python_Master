# 7. 다음과 같은 내용을 지닌 파일 test.txt가 있다.
# 이 파일의 내용 중 'java'라는 문자열을 'python'으로 바꾸어 저장해보자.

f = open("new.txt", 'w')
f.write("Life is too short \n you need java")
f.close()

f = open('new.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('new.txt', 'w')
f.write(body)
f.close()

# 파일 안 값
# Life is too short 
# you need python
# 으로 잘 시행되었음을 알 수 있다.

# 위 코드를 with으로도 한 번 해볼까?

# with open('new_with.txt', 'w') as f:
    #  f.write("I love java")
# with open('new_with.txt', 'r') as f:
    #  body = f.read()
# with open('new_with.txt', 'w' ) as f:
    #  body.replace("java", 'python')
    #  f.write(body)

# 오류 발생: 원인은 body에 replace해준 것을 새 변수에 저장하지 않음
# replace에도 inplace 인수가 있을까?
# 아무튼 다시 시도

with open('new_with.txt', 'w') as f:
    f.write("I love java")
with open('new_with.txt', 'r') as f:
    body = f.read()
with open('new_with.txt', 'w' ) as f:
    body = body.replace("java", 'python')
    f.write(body)

# new_with이란 txt 파일에 "I love python"가 저장되어있다. 기쁘다!