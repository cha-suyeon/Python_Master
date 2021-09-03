# 사칙연산 클래스 만들기

class FourCal:
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

# 클래스 내부에서 구현된 함수는 메서드라고 부른다.

# setdata 메서드의 매개변수
# setdata에는 self, num1, num2의 3개 입력값을 받는다.

# 1. setdata 메서드의 매개변수 

a = FourCal()
print(a.setdata(1,2))

# setdata 메서드에는 self, num1, num2의 총 3개의 매개변수가 필요한데 실제로는 2개만 전달했다.
# 그 이유는 a.setdata(1,2)처럼 호출하면 setdata 메서드의 첫 번째 매개변수 self에는
# setdata 메서드를 호출한 객체 a가 자동으로 전달되기 때문이다.
# 파이썬 메서드의 첫 번째 매개변수 이름은 self를 사용한다.
# 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self를 사용한다.

a = FourCal()
print(FourCal.setdata(a, 4, 2))

# 다음과 같아 클래슬르 통해 메서드를 호출하는 것도 가능하다.
# 하지만 위의 방법은 잘 쓰이지 않는다.
# '클래서이름.메서드' 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해주어야 한다.
# 반면에 '객체.메서드' 형태를 호출할 때는 self를 반드시 생략해서 호출해야한다.

a = FourCal()
print(a.setdata(4,2))
