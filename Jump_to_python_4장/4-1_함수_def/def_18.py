# 다른 예제

def vartest(a):
    a += 1

vartest(3)
print(a)

# 이것도 오류가 발생한다.
# vartest(3)을 수행하면 vartest 함수 안에서 a는 4가 되지만
# 함수 호출 후 print(a)에서 오류가 발생한다.
# 왜냐하면 print 안에서 호출 받아야 하는 a가 무엇인지 알 수 없기 때문에
# 함수 안에서 선언한 매개변수는 함수 밖에서 사용되지 않는다.
