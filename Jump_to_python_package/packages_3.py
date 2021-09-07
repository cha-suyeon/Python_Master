# echo 모듈의 echo_test 함수를 직접 import 하는 방법

from game.sound.echo import echo_test
print(echo_test())

# 하지만 위의 방법은 echo_test 함수를 사용하는 것이 불가능하다.
# import game을 수행하면 game 디렉터리의 모듈 또는 game 디렉터리의 __init__.py에 정의한 것만 참조할 수 있다.
