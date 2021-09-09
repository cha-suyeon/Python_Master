# isintance(object, class), 첫 번쨰 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False

class Person: pass # 아무 기능 없는 person 클래스 생성

a = Person()
print(isinstance(a, Person)) # True 가 나옴

# a가 Person 클래스가 만든 인스턴스 임을 True라고 알려줌

b = 3
print(isinstance(b, Person))

# b가 Person 클래스의 인스턴스가 아닌 것을 False라고 알려줌
