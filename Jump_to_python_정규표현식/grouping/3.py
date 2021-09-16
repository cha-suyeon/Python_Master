import re
p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')
print(m.group(1))
# park
print(m.group(2))
# 010-1234-1234
print(m.group(0))