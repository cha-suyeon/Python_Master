# Set

## 값 1개 추가 ##
s1 = set([1,2,3])
s1.add(4)
print(s1)

## 값 여러 개 추가 ##
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

## 특정 값 제거하기 ##
s1 = set([1,2,3])
s1.remove(2) # 특정 값을 지정해주는 것임
print(s1)