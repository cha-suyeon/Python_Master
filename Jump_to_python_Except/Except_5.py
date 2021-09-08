# IndexError 오류 메시지를 출력하는 소스를 만들어보자

try:
    a = [1,2,3]
    print(a[4])
except IndexError as I:
    print(I)

