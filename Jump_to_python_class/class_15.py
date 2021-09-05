# 클래스 변수
# 객체 변수는 다른 객체들에게 영향 받지 않고 독립적으로 그 값을 유지
# 객체변수와는 성격이 다른 클래스 변수에 대해 알아보자

class Family:
    lastname = "김"

print(Family.lastname)

# 클래스 변수는 위 예와 같이 클래스이름.클래스변수 로 사용 가능함
# 또는 이런 사용도 가능함

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)