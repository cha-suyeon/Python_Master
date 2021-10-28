# Dictionary function

## keys ##
dict = {'name':'Suyeon',"age":25,'birth':1024}
print(dict.keys()) # key 값을 리스트로 반환

for i in dict.keys():
    print(i)

# 리스트 고유의 함수 append, insert, pop, remove, sort 함수는 수행할 수 없음

print(list(dict.keys()))


## values ##
print(dict.values())    # value 리스트
print(dict.items())     # key, value 쌍 얻기
print(dict.clear())     # key:value 쌍 모두 지우기
print(dict)             # None 출력

## key로 value 얻기 ##
dict = {'name':'Suyeon',"age":25,'birth':1024}
print(dict.get('name'))
print(dict.get('birth'))
print(dict.get('hobby'))        # None 출력

print(dict.get('hobby', 'Read')) # Default 값 불러오기
print(dict)                      # 원래 Dictionary에는 영향 없음

## 해당 key가 Dictionary 안에 있는지 조사하기 ##
print('name' in dict)           # 있을 경우 True
print('email' in dict)          # 없을 경우 False
