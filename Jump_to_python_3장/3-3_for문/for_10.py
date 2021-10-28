# 리스트 내포 안에 for문 쓰기
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# if 조건문 하나일 때
# [표현식 for 항목 in 반복 가능 객체 if 조건]

# if 조건문 여러 개 쓰고 싶을 때
# [표현식 for 항목1 in 반복 가능 객체1 if 조건1
#         for 항목2 in 반복 가능 객체2 if 조건2
# ...     for 항목n in 반복 가능 객체n if 조건n]