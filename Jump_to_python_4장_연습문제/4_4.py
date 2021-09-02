# 4. 다음 중 출력 결과가 다른 것 한 개를 골라보자

# 1. print("you" "need" "python")
# 2. print("you"+"need"+"python")
# 3. print("you","need","python")
# 4. print("".join(["you","need","python"]))

# 내가 고른 답: 3번
# 이유: 1,2,4번의 경우 "youneedpython"이 출력된다.
# 3번의 경우 문자열을 ',(콤마)'로 구분해주어서 "you need python"이다.
# 4번의 경우, 리스트라서 "you need python"이 나올 법하지만 "" 띄어쓰기 없이 join 하라는
# 명령 때문에 정답은 3번을 골라보겠다.

# 실행해보면 정답을 알 수 있다...

print("you" "need" "python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))

# 실제로 나온 출력값
# 1. youneedpython
# 2. youneedpython
# 3. you need python
# 4. youneedpython

# 맞추었다!