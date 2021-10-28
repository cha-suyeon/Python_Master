# 8과 같은 방법으로 오류 메시지 가져오기

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

# 결괏값: list index out of range

# 그래서 아까 8번이랑 이거의 차이는
# 지금 as 사용해서 오류 메시지를 보여주는 걸로 바꾼거잖아요 print 대신에
# 그래서 이것도 출력하면 list 오류 메시지만 나오거든요 -> list index out of range 이거

