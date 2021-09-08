# 예외 만들기

# 프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용한다.
# 예외는 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.

class MyError(Exception): # Exception은 파이썬의 내장 클래스
    pass

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

say_nick("천사")
say_nick("바보")

# 저장 후 출력하면 "천사"가 출력하고, MyError가 발생한다.
# MyError 발생을 예외 처리하려면 어떻게 할까? 

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")