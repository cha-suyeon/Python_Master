# Q6.

# a = 4
# try:
#     if a == 4:
#        print('\033[32m'+'Python')
#    elif a == 5:
#        print('\033[32m'+'is')
# except:
#    print('\033[32m'+'fun')

# 해당 코드를 출력하면 Python 이 출력된다.
# fun 이 출력되도록 수정하시오.

try:
    if a == 4:
        print('\033[32m'+'Python')
    elif a == 5:
        print('\033[32m'+'is')
except:
    print('\033[32m'+'fun')

# a가 다른 값일 경우 출력할 값이 없습니다. (else가 처리되어 있지 않음)
# a 변수를 없애주면 try에서 시도할 게 없어, except로 빠져버려 fun이 출력됩니다.