# __init__을 추가한 FourCal() 만들기

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

# __init__ 메서드는 setdata 메서드와 이름만 다르고 모든 것이 동일합니다.
# 단 메서드 이름을 __init__으로 했기 때문에
# 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.

# Quiz!
# a = FourCal() 을 호출 할 때 에러가 나는지?
# ⭕, 이유: 생성자의 매개변수 num1, num2에 해당하는 값이 전달되지 않았기 때문이다.

# 해결 방법
a = FourCal(4,2)

# 위와 같이 수행하면 __init__ 메서드의 매개변수에는 각각 오른쪽 값이 대입된다

# 매개변수       값
#   self   생성되는 객체
#   num1        4
#   num2        2

# 따라서 __init__ 메서드가 호출되면 setdata 메서드를 호출했을 때와 마찬가지로
# num1, num2라는 객체변수가 생성될 것이다.

print(a.num1)
print(a.num2)

print(a.add())
print(a.div())