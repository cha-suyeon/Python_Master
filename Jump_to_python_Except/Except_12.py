# 오류 일부러 발생시키기
# 오류를 일부러 발생 시킬 때도 있다
# 이때 'raise'를 사용한다

# 예를 들어 Bird 클래스 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우에는

class Bird:
    def fly(self):
        raise NotImplementedError

# 위의 예제는 Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현해야 한다는 의지를 보여준다.
# 만약 자식 클래스가 fly 함수를 구현하지 않은 상태로 fly 함수를 호출한다면 어떻게 될까?

class Eagle(Bird): # Eagle 클래스는 Bird 클래스를 상속 받음
    pass

eagle = Eagle()
print(eagle.fly())

# Eagle 클래스는 Bird 클래스를 상속 받는다.
# 그런데 Eagle 클래스에서 fly 함수를 구현하지 않았기 때문에
# Bird 클래스의 fly 함수가 호출된다.
# 그리고 raise에 의해 NotImplementedError 가 발생한다.

# 흐름 이해
# 1. Bird 클래스를 만듦
# 2. Bird 클래스를 상속 받는 자식 클래스 Eagle을 만듦
# 3. Eagle에서 Bird의 fly 함수를 호출함
# 4. fly()가 호출되며 NotImplementedError 가 발생

