# 함수의 결괏값은 언제나 하나

def add_and_mul(a,b):
    return a+b, a*b # 2개의 매개변수를 받아서 더하고 곱한 값을 돌려줌

result = add_and_mul(3,4)
print(result)

# 결괏값은 a+b, a*b로 2개인데 결괏값을 받아들이는 변수로는 result 하나만 쓰였다.
# 하지만 오류는 발생하지 않음
# 그 이유는 함수의 결괏값은 2개가 아니라 언제나 1개라는 데 있다.
# add_and_mul 함수의 결괏값 a+b와 a*b는 튜플 값 하나인 (a+b, a*b)로 돌려준다.
# 따라서 result는 (7, 12)란 값을 가지게 됨

# 만약 이 하나의 튜플 값을 2개의 결괏값처럼 받고 싶다면?

result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)

# 그럼 result1 = 7 , result2 = 12가 됨