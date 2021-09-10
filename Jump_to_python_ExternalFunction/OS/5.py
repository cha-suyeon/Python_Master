# 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen

import os
f = os.popen("dir")
print(f.read()) # 읽어들인 파일 객체의 내용을 보기 위해서 다음과 같이 하면 됨

# os.popen은 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려준다.