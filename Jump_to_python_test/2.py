# Q2 딕셔너리 값 추출하기
# 다음은 딕셔너리의 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.

a = {'A':90, 'B':80}
print(a.get('C', 70))


## 딕셔너리 관련 함수

a = {'name':'suyeon', 'phone':'01012345678','birth':'1024'}

print(a.keys())
print(list(a.keys()))
for i in a.keys():
    print(i)

print(a.values())
for k in a.values():
    print(k)

print(a.items())
print(list(a.items()))

print(a.get('name'))
print(a.get('phone'))
print(a.get('birth'))
print(a.get('email', 'suyeon@gmail.com'))
print(a)

print('name' in a)
print('email' in a)

print(a.clear())
print(a)














