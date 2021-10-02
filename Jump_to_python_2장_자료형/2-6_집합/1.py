# Set

s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

## set의 특징 ##
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다(Unordered)

# set은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
# 딕셔너리도 순서가 없는 자료형이라 인덱싱을 지원하지 않음

l1 = list(s1)
print(l1)
print(l1[0])
print(l1[2])

t1 = tuple(s1)
print(t1)
print(t1[0])
print(t1[2])
