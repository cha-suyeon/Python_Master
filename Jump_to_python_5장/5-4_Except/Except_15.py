# MyError 발생을 예외 처리하기

class MyError(Exception): # Exception은 파이썬의 내장 클래스
    pass

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")



