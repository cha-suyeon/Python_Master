# 곱하기, 빼기, 나누기 기능 만들기

class FourCal:
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # 더하기
    def add(self):
        result = self.num1 * self.num2
        return result

    # 곱하기
    def mul(self):
        result = self.num1 * self.num2
        return result

    # 빼기
    def sub(self):
        result = self.num1 - self.num2
        return result
    
    # 나누기
    def div(self):
        result = self.num1 / self.num2
        return result

a = FourCal()
b = FourCal()
a.setdata(2,4)
b.setdata(3,5)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

# 여기까지가 우리가 목표로 한 사칙연산 기능을 가진 클래스를 만드는 과정이었다!
