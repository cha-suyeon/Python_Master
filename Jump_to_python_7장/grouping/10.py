# 문자열 바꾸기

import re
# sub 매서드
p = re.compile('(blue|white|red)')

print(p.sub('colour', 'blue socks and red shoes'))
# colour socks and colour shoes
print(p.sub('colour', 'blue socks and red shoes', count = 1))
# colour socks and red shoes