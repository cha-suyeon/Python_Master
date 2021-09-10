# Q2. 😡 틀림

# 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스

class MaxLimitCalculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class Limit(MaxLimitCalculator):
    def add(self, val):
        if self.value > 100:
            return 100
        else:
            return self.value

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력

# 정답
# class Limit(MaxLimitCalculator):
#    def add(self, val):
#       if self.value > 100:
#          self.value = 100