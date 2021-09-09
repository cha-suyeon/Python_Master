# eval(expression)은 실행 가능한 문자열(1+2, 'hi', 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.

print(eval('1+2'))
print(eval("'hi'+'a'"))
print(eval('divmod(4, 3)'))

# 보통 eval은 입력 받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.
