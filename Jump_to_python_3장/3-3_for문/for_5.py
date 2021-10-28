# for문과 range 함수
# >>> a = range(10)
# >>> print(a)
# range(0,10)

add = 0 
for i in range(1,11):
    add = add + i
print(add)

# 1~10까지의 합을 더한 값, 55가 출력된다.

add = 0
for i in range(0,10):
    add += i
print(add)