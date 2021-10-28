# IndexError 오류 메시지를 출력하는 소스를 만들어보자

# 답지에 나온 코드

a = [1,2,3]

try:
    print(a[4])
except IndexError as I:
    print(I)

# 차이는 변수 선언을 어디서 하는 지의 차이이며
# list index out of range 라는 결괏값은 같다.