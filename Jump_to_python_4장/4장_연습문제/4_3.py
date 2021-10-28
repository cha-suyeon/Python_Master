# 3. 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
# 오류를 수정하시오

# 제시한 코드
    # input1 = input("첫번째 숫자를 입력하세요:")
    # input2 = input("두번째 숫자를 입력하세요:")
    
    # total = input1 + input2
    # print("두 수의 합은 %s입니다." % total)

# 오류를 잡기 위한 나의 코드

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s입니다." % total)
