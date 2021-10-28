# 변수

## 변수를 만드는 여러 가지 방법

a, b, c = ('python', 'is', 'fun')
print(a)
print(b)
print(c)
print((a,b))

[a, b, c] = ['python', 'is', 'fun']
print(type(a))
print(a)
print(b)

a = b = 'python'
print(a)
print(b)

a = 3
b = 5
print(a)
print(b)

a, b = b, a
print(a)
print(b)
