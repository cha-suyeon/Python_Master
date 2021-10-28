# 입력값의 개수를 모를 때
# 입력값이 여러 개일 때, 그 모든 값을 다 더해주는 함수를 생각해보자

# def 함수이름(*매개변수):
#   수행항 문장

# 여러 개의 입력값을 받는 함수 만들기

def add_money(*args):
    result = 0
    for i in args:
        result = result + i
    return result

# *args처럼 매개변수 이름 앞에 '*'을 붙이면 입력값을 전부 모아서 튜플로 만들어준다.
# 만약 add_money(1,2,3)을 쓰면 (1,2,3)이 된다.
# *args는 임의로 정한 변수 이름이며, 변수 이름은 변경되어도 무관하다.

a = add_money(10000, 3000, 50000)
print(a)