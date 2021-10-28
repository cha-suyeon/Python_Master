# return을 두 개 사용 가능한가?

def add_and_mul(a,b):
    return a+b
    return a*b

# 위처럼 결괏값은 return을 2번하면 되지 않을까?

result = add_and_mul(3,4)
print(result)

# 결괏값으로는 7만 나옴. 이유가 뭘까?
# return a*b는 실행되지 않았다.
# 위의 함수는 결국 return a*b가 없는 함수와 같다.
# 함수는 return문을 만나는 순간! 결괏값을 돌려준 다음에 함수를 빠져나가기 때문이다.
