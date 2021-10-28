# map(f, iterable), 함수 f와 반복 가능한 iterable 자료형을 입력으로 받는다.
# map은 입력 받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.

def two_times(numberlist):
    result = []
    for number in numberlist:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

# 결괏값 [2, 4, 6, 8]
# two_times는 리스트 요소를 입력 받아 각 요소에 2를 곱한 결괏값을 돌려준다.
# 위의 예제를 map으로 바꿔보자