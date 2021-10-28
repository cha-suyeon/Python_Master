# 매개변수에 초깃값 주의할 점
# 조금 다른 형태로 함수의 인수를 전달하는 방법

def say_myself(name, man=True, old):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

print(say_myself("차수연", 25)) # 1번
print(say_myself("차수연", 25, False)) # 2번
print(say_myself("김박사", 50, True)) # 3번

# 앞의 예제와 다른 점은 초깃값 설정의 위치이다.
# 왠지 오류가 발생할 듯
# 오류가 발생한다.
# 이유는 1번을 출력할 경우, 25가 어디에 들어가야 할 지 파이썬은 알 수 없게 된다.
# 오류 메시지: non-default argument follows default argument

# 즉, 매개변수 (name, old, man=True)는 되지만
# (name, man=True, old)는 안 된다고 한다.