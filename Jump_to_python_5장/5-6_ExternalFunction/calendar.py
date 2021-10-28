# calendar

import calendar

# 그해의 전체 달력
print(calendar.calendar(2021))
calendar.prcal(2021)

# 한달 달력
calendar.prmonth(2021,9)

# 요일 정보 반환
# 월~일: 0~6
print(calendar.weekday(2021,9,10))

# 1일의 요일, 그 달이 며칠까지 있는지 반환
print(calendar.monthrange(2021,9))
# 결괏값: (2,30) -> 수요일, 30일

