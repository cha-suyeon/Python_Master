

class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class Limit(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

a = Limit()
a.add(50)
a.add(60)
print(a.value)
