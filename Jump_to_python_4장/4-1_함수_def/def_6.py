# 결괏값이 없는 함수 2

def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

a = add(3,4)
print(a)

# 이렇게 해도 수행할 문장1과 None이 나옵니다.
# a의 값이 None인 이유는 add 함수에서 결괏값이 없기 때문에 None을 반환한다.