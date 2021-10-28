# 매개변수 지정하여 호출

def add(a,b):
    return a+b

result = add(a=3, b=7) # a에 3, b에 7을 전달
print(result)

# 이런 식으로 매개변수 값을 직접 지정하여 잔달할 수 있다.
# 또한 이 방식은 매개변수 순서를 상관하지 않아도 된다.

result2 = add(b=7, a=3)
print(result2)