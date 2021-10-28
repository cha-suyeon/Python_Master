# id(object), 객체를 입력 받아 객체의 고유 주소 값을 돌려주는 함수이다.

a = 3 
b = 3 
c= a

print(id(a))
print(id(b))
print(id(c))

# 위 3개의 id 값은 모두 동일하다.
# a, b, c가 모두 같은 객체를 가리키기 때문에

print(id(4))

# 만약 id 에 다른 객체 4를 넣어주면 당연히 다른 결괏값이 나온다.
