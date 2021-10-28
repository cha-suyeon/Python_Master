# 게시물의 총 건수와 한 페이지에 보여 줄 게시물 수를 입력으로 주었을 때 총 페이지수를 출력하는 프로그램

# 게시물의 총 건수 : m
# 페이지당 보여줄 게시물 수 : n
# 총 페이지 수 : 구하셈

def total(m, n):
    if m % n == 0 :
        return m // n
    else:
        return m // n + 1

print(total(5,10))
print(total(15,10))
print(total(25,10))
print(total(30,10))