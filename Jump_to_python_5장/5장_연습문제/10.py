# Q10. 😡 틀림. 못 씀.

import os

# 1. C:\doit 디렉터리로 이동
os.chdir('C:\doit')

# 2. dir 명령을 실행하고 그 결과를 변수에 담음
result = os.popen("dir")

# 3. dir 명령의 결과를 출력함
print(result.read())