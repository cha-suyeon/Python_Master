# 아까 say_nick을 예외 처리 만들어주면서 오류 메시지를 출력해보기

class MyError(Exception): # Exception은 파이썬의 내장 클래스
    pass

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

# 그런데 여기서 오류 메시지가 출력되지 않는다.
# 오류 메시지를 출력했을 때 오류 메시지가 보이게 하려면 어떻게 해야할까?
# 오류 클래스에 __str__ 같은 메서드를 구현해야 한다.
# __str__ 메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드이다.
