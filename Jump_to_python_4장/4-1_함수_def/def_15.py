# 매개변수에 초깃값 미리 설정하기
# 조금 다른 형태로 함수의 인수를 전달하는 방법

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

# say_myself 함수는 3개의 매개변수를 받아서
# 마지막 인수인 man이 True이면 "남자", False이면 "여자를 출력"

# man = True 는 매개변수에 미리 값을 넣어주어서 초깃값을 설정하는 방법이다.

print(say_myself("차수연", 25))
print(say_myself("차수연", 25, False))
print(say_myself("김박사", 50, True))

# 초깃값에 False를 넣어주면 "여자입니다" 가 출력된다.