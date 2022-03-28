# Q6 숫자의 총합 구하기
# 사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오. (단 숫자는 콤마로 구분하여 입력한다.)

n = map(int, input().split(','))
print(sum(n))

## 교재에 제시된 정답

user = input("숫자를 입력하세요:")
numbers = user.split(',')
total = 0
for n in numbers:
    total += int(n)
print(total)


## 더 깔끔하게 만들어보기

user = int(input("숫자를 입력하세요:"))
numbers = user.split(',')
total = 0
for n in numbers:
    total += n
print(total)

## 더 깔끔하게 만들어보기 2

numbers = input().split(',')
total = 0
for n in numbers:
    total += int(n)
print(total)