
class FourCal:
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    # 더하기 기능 만들기
    def add(self):
        result = self.num1 + self.num2
        return result


a = FourCal()
a.setdata(4,2)
print(a.add())

# add 메서드의 매개변수는 self이고 반환 값은 result이다.
# 반환 값인 result를 계산하는 부분은 아래와 같다.
# result = self.num1 + self.num2 

# a.add()와 같이 a 객체에 의해 add 메서드가 수행되면
# add 메서드의 self에는 객체 a가 자동으로 입력된다.

# 그래서 result = self.num1 + self.num2는
# result = a.num1 + a.num2 와 같다.