# 메서드 오버라이딩

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


# a = FourCal(4,0)
# print(a.div())

# 위를 수행하면 ZeroDivisionError가 뜬다
# 0으로 나누어도 오류가 아닌 값을 돌려주려면?

class SafeFourCal(FourCal):
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2

# FourCal을 상속하는 클래스를 추가로 만들었고
# div 메서드를 동일한 이름으로 다시 작성하였음
# 이런 작업을 '메서드 오버라이딩'이라고 하며
# 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 뜻함
# 이렇게 메서드를 오버라이딩하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출됨

a = SafeFourCal(4,0)
print(a.div())