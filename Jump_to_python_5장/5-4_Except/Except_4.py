# try :
#       오류가 발생할 수 있는 구문
# except Exception as e:
#       오류 발생
# else:
#       오류 발생하지 않음
# finally:
#       무조건 마지막에 실행

# 위는 오류 처리를 위한 try, except문의 기본 구조입니다.
# try 블록 수행 중 오류가 발생하면 except 블록이 수행됩니다.
# 하지만 try 블록에서 오류가 발생하지 않으면 except 블록은 수행되지 않습니다.

# except [발생오류 [as 오류 메시지 변수]]:
# except 구문 사용법 3가지

# 1. try, except만 쓰는 방법
# try:
#       ...
# except:
#       ...
# 이 경우는 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.

# 2. 발생 오류만 포함한 except문
# try:
#       ...
# except 발생 오류:
#       ...
# 이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행한다는 뜻이다.

# 3. 발생 오류와 오류 메시지 변수까지 포함한 except문
# try:
#       ...
# except 발생 오류 as 오류 메시지 변수:
# 이 경우는 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다.

# 예시
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# 출력값은 'division by zero'이 나옵니다.
# 왜냐하면 try시 ZeroDivisionError가 발생하여 except 블록이 실행되고
# 변수 e에 담기는 오류 메시지를 위와 같이 출력합니다.