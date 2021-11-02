# Q3 리스트의 더하기와 extend 함수
# +, extend 차이

a = [1, 2, 3]
a = a + [4,5]
print(a)
# [1, 2, 3, 4, 5]

a = [1, 2, 3]
a.extend([4,5])
print(a)
# [1, 2, 3, 4, 5]

# 차이점
# +를 사용하면 리스트 a의 값이 변하는 것이 아니라 두 리스트가 더해진 새로운 리스트가 반환된다.
# extend를 사용하면 리스트 a의 주소 값이 변하지 않고 유지됨


b = [1,2,3]
print('original id:', id(b))
b = b + [[4,5]]
print('b:', b)
print('+ id:', id(b))

b = [1,2,3]
print('original id:', id(b))
b.extend([4,5])
print('b:',b)
print('extend id:', id(b))

b = [1,2,3]
print('original id:', id(b))
b.append([4,5])
print('b:',b)
print('append id:', id(b))

# 리스트에 +를 사용할 때와, extend/append 함수의 차이
# append는 매개변수 그 자체를 원소로 넣고, extend는 가장 바깥쪽 iterable을 넣음
# append는 그대로 원소를 집어넣고, extend는 가장 바깥쪽 iterable의 모든 항목을 넣음

x = [1,2,3]
y = 'ping'
x.append(y)
print('append:',x)

x = [1,2,3]
y = 'ping'
x.extend(y)
print('extend:',x)



























