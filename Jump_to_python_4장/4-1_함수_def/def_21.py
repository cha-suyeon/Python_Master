# lambda 

# lambda 함수를 생서할 때 사용하는 예약어로 def와 동일한 역할을 한다
# 보통 함수를 한 줄로 간결하게 만들 때 사용한다
# 람다 라고 읽으며 def를 사용할 정도로 복잡하지 않을 때 주로 사용된다

# 사용법
# lambda 매개변수1, 매개2, 매개3, ... : 매개변수를 사용한 표현식

add = lambda a, b: a-b
result = add(3,5)
print(result)