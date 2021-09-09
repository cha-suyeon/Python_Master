# sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려줌

print(sorted([3,1,2])) # [1, 2, 3]
print(sorted(['a','c','b'])) # ['a', 'b', 'c']
print(sorted("zero")) # ['e', 'o', 'r', 'z']
print(sorted((3,2,1))) # [1, 2, 3]

# 리스트 자료형에서도 sort 함수가 있다. 하지만 리스트 자료형의 sort 함수는 리스트 객체 자체만 정렬할 뿐 정렬된 결과를 돌려주지는 않음
