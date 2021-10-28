# sys 모듈로 매개변수 주기

import sys

args = sys.argv[1:]
for i in args:
    print(i)

# sys 모듈을 사용하면 매개변수를 직접 줄 수 있다.
# sys 모듈 사용 시, import sys 필수이다.

# 위의 예는 입력받은 인수를 for문을 사용해 차례대로 하나씩 출력하는 예이다.
# sys 모듈의 argv는 명령 창에서 입력한 인수를 의미한다.
# 즉, 다음과 같이 입력했다면 argv[0]은 파일 이름 sys1.py가 되고
# argv[1]부터 뒤에 오는 인수가 차례대로 argv의 요소가 된다.

# sys1.py - argv[0]
# aaa - argv[1]
# bbb - argv[2]
# ccc - argv[3]
