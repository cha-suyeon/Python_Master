# Q13. 😡 틀림... 갈 길이 멀다...

# random 모듈을 사용하여 로또 번호 1~45 사이의 숫자 6개를 중복된 값 없이 생성해보자.


import random

result = [] # 결괏값을 넣어줄 빈 리스트 생성

while len(result) < 6: # result 의 길이가 6 미만이면 계속 시행
    num = random.randint(1, 45) # 1부터 45까지 난수 생성
    if num not in result: # result에 num이 없다면, num을 result에 추가
        result.append(num) # 중복값은 들어가지 않는다.

print(result) # 결괏값 출력
