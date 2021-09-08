# 오류 회피하기 with pass
# 프로그래밍을 하다보면 특정 오류가 발생할 경우 그냥 통과 시켜야 할 때가 있다.

try:
    f.open = ("없는 파일", 'r')
except FileNotFoundError:
    pass

# 파일이 없더라도 오류를 발생시키지 않고 통과한다
# try문 안에서 FileNotFoundError가 발생할 경우, pass를 사용하여 오류를 그냥 회피하도록 한 예제이다.

