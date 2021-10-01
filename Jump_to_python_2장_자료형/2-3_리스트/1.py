# 2-3 리스트

a = [1,2,3,['a','b','c']]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])
print(a[3][2])
print(a[-1][-1])

# 리스트 수정과 삭제
a = [1,2,3]
del a[1]
print(a)

a = [1,2,3,4,5]
del a[2:]
print(a)