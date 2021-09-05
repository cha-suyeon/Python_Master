# 클래스 변수 변경

class Family:
    lastname = "김"

Family.lastname = "박"

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

# 클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastname 값도 모두 변경되었음!
# 즉, 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있음

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))

# id 값이 모두 같으므로 위 세 개는 같은 메모리를 가리키고 있음
# 클래스 변수를 가장 마지막에 설명하는 이유는 클래스 변수보다 클래스 객체변수가 둬 중요하기 때문!
