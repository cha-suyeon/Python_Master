# while문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: continue
    print(a)

# while문을 빠져나가지 않고 맨 처음 조건으로 돌아가게 만들고 싶은 경우이다.
# 이때 사용하는 것이 continue문이다.
# a가 1씩 증가하며 참이 되는 경우 a가 짝수일 때 continue 문장 수행
# 그래서 a가 짝수일 때는 print(a)가 수행되지 않는다.