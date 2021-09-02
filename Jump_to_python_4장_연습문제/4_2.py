# 2. 입력으로 들어오는 모든 수의 평균 값을 계산해주는 함수를 작성해보자.

def avg_num(*args):
    result = 0
    for i in args:
        result += i
    return (result/len(args))

print(avg_num(1,2))
print(avg_num(1,2,3,4,5))


# 안 보고 다시 작성해보기

def avg_num(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

print(avg_num(3,5))
print(avg_num(4,4,4,4))

# return 들여쓰기를 못해서 또 틀렸음...