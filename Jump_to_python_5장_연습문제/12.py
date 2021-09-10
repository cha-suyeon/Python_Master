# Q12.

# time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력

# 내가 쓴 코드
# import time
# print(time.strftime('%c', time.localtime(time.time())))

# 정답 코드
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))