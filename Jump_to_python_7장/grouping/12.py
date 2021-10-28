# sub 매서드 사용 시 참조 구문 사용하기

import re

p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')

print(p.sub('\g<phone> \g<name>', 'park 010-1234-1234'))
# 010-1234-1234 park
print(p.sub('\g<2> \g<1>', 'park 010-1234-1234'))
# 010-1234-1234 park