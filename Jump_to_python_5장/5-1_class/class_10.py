# 생성자(Constructor)

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
a.setdata(1,2)
print(a.add())

# Error가 발생한다.
# 에러명: 'FourCal' object has no attribute 'num1'
# 에러가 난 이유는 FourCal 클래스의 인스턴스 a에
# setdata라는 메서드를 수행하지 않고 add 메서드를 시행했기 때문
# setdata 메서드를 수행해야 객체 a의 객체변수 num1, num2가 생성됨
# 그러므로 a.setdata()가 필요함

# 이런 경우에 객체의 초깃값을 설정해야 하는 경우인데
# setdata같은 메서드를 호출하여 초깃값을 설정하기 보다는
# 생성자를 구현하는 것이 안전한 방법이다

# 생성자(Conductor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미함
# 파이썬 메서드 이름으로 __init__을 사용하면 이 메서드는 생성자가 된다
