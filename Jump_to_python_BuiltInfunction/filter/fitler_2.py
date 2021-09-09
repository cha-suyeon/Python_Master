# filter 함수 사용 2

def positive(x):
    return x > 0

print(list(filter(positive, [1,-3,-2,0,-5,6])))

