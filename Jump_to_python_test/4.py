# Q4 리스트 총합 구하기
# 다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상 점수의 총합을 구하시오.

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

sum = 0
for i in A:
    if i >= 50:
        sum += i
    
print(sum)


## while문을 사용한 리스트 총합 ## 

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

result = 0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark

print(result)