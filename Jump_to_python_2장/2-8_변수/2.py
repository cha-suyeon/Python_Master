# 변수

## [:] 이용 ##
a = [1,2,3]
b = a[:]
a[1] = 4
print(a)
print(b)

# a 리스트를 바꾸더라도 b에 영향을 주지 않음
# [:]을 사용해서 복사했기 때문에

## copy 모듈 사용 ##
from copy import copy
a = [1,2,3]
b = copy(a)

print(b is a)

# a와 b 객체는 서로 다름
# copy(x)는 copy 모듈이고
# a.copy() 는 리스트 자료형 자체 함수임

c = a.copy
print(c is a)
