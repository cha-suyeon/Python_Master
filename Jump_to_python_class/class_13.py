# 원래 목적인 a의 b제곱을 계산하는 MoreFourCal 만들기

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

class MoreFourCal(FourCal):
    def pow(self):
        result = self.num1 ** self.num2
        return result

a = MoreFourCal(4,2)
print(a.pow())

# MoreFourCal 클래스로 만든 a 객체에 값 4,2를 설정한 후 pow 메서드를 호출하면 16을 돌려준다.
# 상속은 MoreFourCal 클래스처럼 기존 클래스(FourCal)는 그대로 놔둔 채
# 클래스의 기능을 확장시킬 때 주로 사용함