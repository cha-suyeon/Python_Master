# random_pop.py
# pop 메서드에 의해 꺼내진 요소는 삭제된다.

import random

def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

if __name__ == '__main__':
    data = [1,2,3,4,5]
    while data : print(random_pop(data))

# 위 함수는 리스트의 요소 중에서 무작위로 하나를 선택해서 꺼냄
# 꺼낸 값을 pop 해서 값을 돌려줌
# pop 메서드에 의해 사라짐
