# 결괏값을 유지하기 위해 result에 global을 사용

result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))