# Q2. π‘ νλ¦Ό

# κ°μ²΄λ³μ valueκ° 100 μ΄μμ κ°μ κ°μ§ μ μλλ‘ μ ννλ MaxLimitCalculator ν΄λμ€

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 λνκΈ°
cal.add(60) # 60 λνκΈ°

print(cal.value) # 100 μΆλ ₯

# μ λ΅
# class Limit(MaxLimitCalculator):
#    def add(self, val):
#       if self.value > 100:
#          self.value = 100