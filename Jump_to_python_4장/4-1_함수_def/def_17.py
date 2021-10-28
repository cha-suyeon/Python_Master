# 함수 안에서 선언한 변수의 효력 범위
# vartest.py
a = 1 # 함수 밖의 변수 a
def vartest(a): # vartest 함수 선언
    a += 1

vartest(a) # vartest 함수의 입력값으로 a를 줌
print(a) # a값 출력

# vartest는 결괏값이 없는 함수이다.
# 결괏값으로는 1이 나온다.
# 함수 안의 a는 함수 안에 있는 a 이기 때문이다.
# 즉, def vartest(a)에서 입력값을 전달받는 매개변수 a는
# 함수 밖의 변수 a와 다르다!

