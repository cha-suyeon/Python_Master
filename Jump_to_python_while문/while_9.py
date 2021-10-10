number = 358

rem = rev = 0

for i in range(3):
    rem = number % 10
    print(rem)
    rev = rev * 10 + rem
    print(rev)
    number = number // 10
    print(number)

print(rev)