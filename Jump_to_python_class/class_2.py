# 2대의 계산기가 필요한 상황이라면?
# 각 계산기는 각각의 결괏값을 유지해야 하기 때문에
# add 함수 하나만으로 결괏값을 따로 유지할 수 없다.

result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# 똑같은 일을 하는 add1, add2 함수를 만들었다.
# 각 함수에서 계산한 결괏값을 유지하면서 저장하는
# 전역 변수 result1, result2가 필요하게 되었다.

# 계산기1의 값이 계산기 2에 아무 영향을 끼치지 않음
# 하지만 계산기가 3, 5, 10개로 점점 더 많이 필요해진다면?
# 그때마다 전역 변수와 함수를 추가할 것인지?
# 여기에 빼기와 곱하기 등을 더한다면 더 복잡해질 것이다.