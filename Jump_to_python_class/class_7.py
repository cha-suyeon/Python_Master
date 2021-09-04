# setdata 메서드의 수행문

class FourCal:
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

a = FourCal()
b = FourCal()

a.setdata(4,2)
print(a.num1)

b.setdata(3,7)
print(b.num1)

# a, b 객체의 각각 num1 값이 출력된다.
# 이로써 알 수 있는 것은 a 객체의 first 값은 b 객체의 first 값에 영향 받지 않고 값을 유지한다는 것이다.
# 클래스로 만든 객체의 객체 변수는 다른 객체의 객체 변수에 상관없이 독립적인 값을 유지한다.
# id 함수를 사용하면 객체 변수가 독립적인 값을 유지한다는 점을 볼 수 있다.

print(id(a.num1))
print(id(b.num1))

# a객체의 num1 주소 값과 b객체의 num1 주소값이 서로 다르므로 각각 다른 곳에 그 값이 저장됨
# 객체 변수는 그 객체의 고유값을 저장할 수 있는 공간이다.
# 객체 변수는 다른 객체들 영향 받지 않고 독립적으로 그 값을 유지한다.
