# 함수 안에서 함수 밖의 변수를 변경하는 방법

a = 1
def vartest(a):
    a += 1
    return a

a = vartest(a)
print(a)

# 이렇게 코드를 작성할 경우 결괏값이 2로 정상적으로 나온다.
# 첫 번째 방법은 return을 사용하는 방법이었다.
# vartest 함수는 입력으로 들어온 값이 1 을 더해주고 반환해준다.
