# __all__ 추가
# __all__의 의미: sound 디렉터리에서 * 기호를 사용하여 import 할 경우
# 이곳에 정의된 echo 모듈만 import 된다는 의미

# from game.sound.echo import * 는 __all__과 상관없이 무조건 import된다
# 이렇게 __all__ 과 상관없이 무조건 import 되는 경우는
# from a.b.c import * 에서 c가 모듈인 경우이다.

__all__ = ['echo']

# 위처럼 해당 파일 __init__.py를 수정하면 아까 원하던 결과가 출력될 것임

# >>> from game.sound.echo import *
# >>> print(echo.echo_test())
# echo