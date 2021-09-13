# Q8. 

code = """
from datetime import date, timedelta

filter_day7 = []
filter_d7 = 0

for i in range(0, 8):
    today_date = date.today() - timedelta(filter_d7)
    real_time = today_date.strftime('%Y-%m-%d')
    filter_day7.append(real_time)
    filter_d7 = filter_d7 + 1

result = ', '.join(filter_day7)
print(result)
"""

# 위의 code 출력 시, 어떤 결괏값이 나오나요?

# 2021-09-12, 2021-09-11, 2021-09-10, 2021-09-09, 2021-09-08, 2021-09-07, 2021-09-06, 2021-09-05

# 1. for문 이해
# 2. 날짜 형식 지정에 대한 이해
# 3. 리스트에 append 이해
# 4. join에 대한 이해
