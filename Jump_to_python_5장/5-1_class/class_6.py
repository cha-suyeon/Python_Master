# setdata 메서드의 수행문

class FourCal:
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

# setdata(1,2)의 의미는
# self.num1 = 1
# self.num2 = 2
# 와 같습니다.

# self는 전달된 객체 a이므로
# a.num1 = 1
# a.num2 = 2
# 와 같습니다.
# 확인해볼까요?

a = FourCal()
a.setdata(4,2)
print(a.num1)
print(a.num2)

# 4, 2가 정상적으로 출력합니다.
# a 객체에 객체변서 num1, num2가 생성되었음을 확인할 수 있습니다.

