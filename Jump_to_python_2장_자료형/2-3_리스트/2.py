# 리스트 관련 함수
## append
a = [1,2,3]
a.append(4)
print(a)
a.append(None)
a[4] = 5
print(a)
a.append([6,7])
print(a)

## sort
a = [1,4,5,2,4]
a.sort()
print(a)

a = ['a', 'z', 'c', 'e', 'b']
a.sort()
print(a)

## reverse
a = ['a', 'c', 'b']
a.reverse()
print(a)

## index
a = [1,2,3]
print(a.index(3))
print(a.index(2))

## insert
a.insert(0,4)
print(a)
a.insert(5,1)
print(a)
a.insert(10000,6) # 맨 마지막에 값 삽입
print(a)
a.insert(-1, 2) # 끝에서 1번째 전에 추가
print(a)

## remove
a = [1,2,3,1,2,3]
a.remove(3)
print(a)

a = [1,2,3,3,3,3,3,3]
for i in range(len(a)):
    a.remove(3)
    print(a)
    if not 3 in a:
        break

## pop
a = [1,2,3]
a.pop()
print(a)

a = [1,2,3,4,5]
b = a.pop()
print(a)
a.append(b)
print(a)

## count
a = [1,2,3,4,5,1,1,1,1,1]
print(a.count(1))

## extend
a = [1,2,3]
a.extend([4,5])
print(a)
b = [6,7]
a.extend(b)
print(a)