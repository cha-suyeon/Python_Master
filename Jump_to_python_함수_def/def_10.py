# 여러 개의 입력값을 받고 싶을 때 2
# 앞에서의 예시처럼 *args의 방법만 있는 것은 아니다.
# 아래의 예시를 통해 더 다양한 방법을 보자

def add_mul(choice, *args):
    if choice == "add": # 매개변수 choice에 "add"를 입력 받는 경우
        result = 0
        for i in args:
            result += i # args에 입력받은 모든 값을 더한다.
    elif choice == "mul": # 매개변수 choice에 "mul"를 입력 받는 경우
        result = 1
        for i in args:
            result *= i # *args에 입력받은 모든 값을 곱한다.
    return result


result = add_mul('add', 1,2,3,4,5,6)
print(result)
result1 = add_mul('mul', 1,2,3,4,5,6)
print(result1)

# add_mul 함수는 여러 개의 입력값을 의미하는 *args 매개변수 앞에 choice 매개변수가 추가되었다.
# 매개변수 choice에 'add'가 입력된 경우에 *args에 입력되는 모든 값을 더해서 도렬주고
# 'mul'이 입력된 경우에 *args에 입력되는 모든 값을 곱해서 돌려준다.
