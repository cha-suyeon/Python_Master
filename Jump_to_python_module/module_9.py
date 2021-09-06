# 클래스나 변수 등을 포함한 모듈

import module_8

# 변수 PI의 값이 출력된다.
print(module_8.PI)

# module_8에 있는 Math 클래스를 사용하는 방법
a = module_8.math()
print(a.solv(2))

# 위처럼 모듈 안에 있는 클래스를 활용하려면 모듈 이름을 먼저 입력해주어야 한다.

# module_8 안에 있는 함수 add 사용하기
print(module_8.add(5,5))
print(module_8.add(module_8.PI, 4.4))
