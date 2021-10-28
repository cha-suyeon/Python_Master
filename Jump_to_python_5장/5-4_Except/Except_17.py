
# __str__ 같은 메서드
# __str__ 메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드이다.

class MyError(Exception): # Exception은 파이썬의 내장 클래스
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)