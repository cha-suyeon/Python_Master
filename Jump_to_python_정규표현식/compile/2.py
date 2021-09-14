import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)
