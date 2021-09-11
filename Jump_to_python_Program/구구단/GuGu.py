# 2단을 출력하는 구구단 만들기

def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result

print(GuGu(2))