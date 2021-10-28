# ZeroDivisionError, IndexError 함께 처리하기

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)