# 클래스를 사용해서 앞의 예제를 해결해보자

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    # 빼기 추가하기
    def sub(self, num):
        self.result -= num
        return self.result
        
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 앞서 함수 2개를 사용했을 때와 동일한 결과가 출력된다.
# Calculator 클래스로 만든 별개의 게산기 cal2, cal2가 각각의 역할을 수행함
# 클래스를 사용하면 계산기 대수가 늘어나더라도 객체를 생성만 하면 되기 때문에
# 함수를 사용하는 경우와 달리 매우 간단해진다.
# 빼기 기능을 더하려면 Calculator 클래스에 다음과 같은 기능을 추가하면 된다.