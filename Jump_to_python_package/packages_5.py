# __init__.py 의 용도
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
# 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 __init__.py이 없다면 패키지로 인식되지 않음

from game.sound import *
print(echo.echo_test())

# error 발생
# 분명 game.sound 패키지에서 모든 것을 import 하여서 echo 모듈을 사용할 수 있어야 하는데
# echo라는 이름이 정의되지 않았다는 NameError가 뜸

# 이렇게 특정 디렉터리의 모듈을 *을 사용하여 import 할 때는
# 다음과 같이 __init__.py 파일에 __all__ 변수를 설정하고
# import 할 수 있는 모듈을 정의해 주어야 함


