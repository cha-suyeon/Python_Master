# NotImplementedError 가 발생하지 않게 하려면 다음과 같이 Eagle 클래스에 fly 함수를 반드시 구현해야 한다.

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()