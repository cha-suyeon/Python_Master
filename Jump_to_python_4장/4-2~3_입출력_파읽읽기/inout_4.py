# 큰 따옴표("")로 둘러싸인 문자열은 + 연산과 동일하다

print("Life is wonderful.")
print("Life"+"is"+"wonderful.")

# Life is wonderful.
# Lifeiswonderful.
# 출력값은 다르다. 띄어쓰기가 없다.

# 띄어쓰기를 하는 방법 -> ',' 콤마 사용

print("Life is wonderful.")
print("Life","is","wonderful.")

# Life is wonderful.
# Life is wonderful.
# 동일한 출력값이 나온다.

# 한 줄에 결괏값 출력하기
# for문 배울 때 구구단에서 보았듯이 한 줄에 결괏값을 계속 이어서 출력하려면
# 매개변수 end를 사용하여 끝 문자를 지정해야 한다.

for i in range(10):
    print(i, end=' ')

# 0 1 2 3 4 5 6 7 8 9 