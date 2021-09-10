# time

# time
import time

# time.time
# time은 UTC를 사용하여 현재 시간을 실수 형태로 돌려주는 함수
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴
print(time.time())

# time.localtime
# time.time()으로 반환된 실수로 연도, 달, 월, 시, 분, 초 로 바꾸어주는 함수
print(time.localtime(time.time()))

# time.asctime
# time.localtime()에 의해서 반환된 튜플 형태 값으로 알아보기 쉬운 형태로 리턴하는 함수
print(time.asctime(time.localtime(time.time())))

# time.ctime : 현재 시간 리턴
# time.asctime(time.localtime(time.time()))과 같음
# time.asctime과 다른 점은 ctime은 항상 현재 시간만 돌려줌
print(time.ctime())

# 시간에 관계된 것을 세밀하게 표현할 수 있는 여러가지 포맷 제공
print(time.strftime('%x', time.localtime(time.time()))) # 현재 설정된 지역에 기반한 날짜 출력
print(time.strftime('%c', time.localtime(time.time()))) # 날짜와 시간 출력
