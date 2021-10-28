# 변수

a = 1           # 정수형 변수 
b = 'python'    # 문자열 변수
c = [1,2,3]     # 리스트 자료형 변수

print(type(a))  # int
print(type(b))  # str
print(type(c))  # list

a = [1,2,3]
print(id(a))

b = a
print(id(b))

print(a is b)
a[1] = 4
print(a)
print(b)