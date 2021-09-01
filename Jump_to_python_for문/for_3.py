# for문 응용
marks = [90, 25, 67, 45, 80] # 학생들의 시험 점수 리스트
number = 0 # 학생에게 보여 줄 번호
for mark in marks: # 리스트 순서대로 mark에 대입
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)