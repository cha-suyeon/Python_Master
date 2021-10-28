# relative 패키지

# 만약 graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면?
# render.py를 수정해야함. 

from game.graphic.render import render_test
print(render_test())
