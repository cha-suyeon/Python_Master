# bool

## 자료형의 참과 거짓 ##

# 'python' : True
# "" : False
# [1,2,3] : True
# [] : False
# () : False
# {} : False
# 1 : True
# 0 : False
# None : False

a = [1,2,3,4,5]
while a:
    print(a.pop())

a = [1,2,0,3,4,5]
while a:
    print(a.pop())

# a가 빈 리스트가 될 때까지 while 문 수행

if [1,2,3]:
    print("True")
else:
    print("False")

# [1,2,3] 이 빈 리스트가 아니여서 True이기 때문에 True 반환

