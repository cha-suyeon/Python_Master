# 클래스의 상속
# 상속(Inheritance)이란? 물려받다의 의미이다.

# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것
# 이번에는 상속 개념을 사용하여 우리가 만든 FourCal 클래스에 a**b를 구할 수 있는 기능을 추가해보자

# 만든 FourCal 클래스 가져오기
class FourCal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        result = self.num1 + self.num2
        return result
    def mul(self):
        result = self.num1 * self.num2
        return result
    def sub(self):
        result = self.num1 - self.num2
        return result
    def div(self):
        result = self.num1 / self.num2
        return result

# FourCal 클래스를 상속하는 MoreFourCal 클래스 만들기
class MoreFourCal(FourCal):
    pass

# 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
# class 클래스 이름(상속할 클래스 이름)
# MoreFourClass는 FourClass를 상속했으므로 FourCal의 모든 기능을 사용할 수 있어야 합니다.

a = MoreFourCal(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# 상속 받은 FourClass 기능을 모두 사용 가능하다.
