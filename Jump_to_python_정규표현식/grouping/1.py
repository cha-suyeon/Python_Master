import re

p = re.compile('(ABC)+')
m = p.search("ABCABCABC OK?")
print(m)
print(m.group(0))