# choice 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택해서 리턴

import random

def random_pop(data) :
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == '__main__':
    data = [1,2,3,4,5]
    while data : print(random_pop(data))