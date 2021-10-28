# 1. 주어진 자연수가 홀수인지 짝수인지 판별해주는 is_odd 함수 만들기

def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

print(is_odd(3))
print(is_odd(4))
