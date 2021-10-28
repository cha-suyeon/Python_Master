# 입력하는 값의 단 만들기
result = []
n = int(input('몇 단을 만들고 싶으십니까?'))
for i in range(1,10):
    num = n * i
    result.append(num)
print(result)

# 2~9단까지 만들기
for i in range(2, 10):
    for n in range(1, 10):
        print(i, '*', n, '=', i*n)

# 2~9단 더 예쁘게 만들기
for i in range(2, 10):
    print('-----', i, '단입니다-----')
    for n in range(1, 10):
        print(i, '*', n, '=', i*n)

# 2~9단 리스트에 모두 담기
result = []
for i in range(2, 10):
    for n in range(1, 10):
        num = n * i
        result.append(num)
print(result)

# while문으로 해보기
i = 1
while i < 9:
    i += 1
    j = 1
    print('-----', i, '단입니다-----')
    while j < 10:
        print(i, '*', j, '=', i*j)
        j += 1

# 입력받은 수가지만 구구단 출력하기 +) break
x = int(input('몇 단까지 원하시나요?==>'))
i = 1
while i < 9:
    i += 1
    j = 1
    print('---', i, '단입니다---')
    while j < 10:
        print(i, '*', j, '=', i*j)
        j += 1
    if i == x:
        break
