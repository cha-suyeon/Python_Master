import re

p = re.compile('[a-z]+')
m = p.search("python")
print(m)