# 5. A 학습에 총 10명의 학생이 있다. 학생들의 중간고사 점수는 아래와 같고
# for문을 사용하여 A 학급의 평균 점수를 구해보자.

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = (total/len(A))
print(average)