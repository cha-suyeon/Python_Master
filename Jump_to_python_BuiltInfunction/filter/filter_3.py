# lambda를 사용한 filter

print(list(filter(lambda x : x > 0, [1,-3,2,0,-5,6])))


# 생각해보니 이 filter라는 것 여러 번 배웠었다.
# 나는 이 'filter'를 배울 때마다 헷갈렸다.
# filter란 이름을 가진 함수도 진짜 존재하고,
# 특정 조건으로 걸러서 걸러진 요소들로 iterator객체를 만드는 것도 filter라고 한다.

# filter 내가 배운 내용으로만 생각하면 크게 세 가지가 있는 것 같다.
# 1. 특정 조건으로 걸러진 연산을 뽑아주게 만들어주는 것 자체를 filter라 함
# 2. filter(첫 번째 함수, 반복 가능한 자료형)
# 3. lambda를 사용한 filter