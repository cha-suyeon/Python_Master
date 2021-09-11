# 2단부터 9단까지 출력해보기

print("2단부터 9단까지 구구단을 외자")

for i in range(2, 10):
    print(i, "단입니다.")
    for x in range(1, 10):
        print(i, 'x', x, '=', i*x)