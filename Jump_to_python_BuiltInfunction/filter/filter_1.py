# filter, 첫 번째 인수는 함수 이름, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형
# 두 번째 반복 가능한 자료형 요소가 첫 번째 인수인 함수 자리에 들어가면 반환 값이 참인 것만 묶어서 돌려준다.

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))

# 흐름 정리
# 1. positive라는 함수를 생성한다.
# 2. 빈 리스트 result 생성
# 3. l 만큼 i를 반복
# 4. 대신 i가 0보다 클 때 result에 i를 추가한다.
# 5. l에 [1,-3,2,0,-5,6] 이란 리스트를 넣어주고 0보다 큰 값을 반환한다.
