# import 모듈 이름
# 모듈이름.함수이름

# 위처럼 말고 바로 함수 이름만 쓰고 싶을 때는?
# from 모듈 이름 import 모듈 함수

from module_1 import add, sub

print(add(3,5))
print(sub(5,7))

# 2가지 방법이 있음
# 1. from 모듈이름 import 함수1, 함수2, ...
# 2. form 모듈이름 import *
# 두 번째 방법은 * 문자를 사용하는 방법
# * 문자의 의미는 everything!
