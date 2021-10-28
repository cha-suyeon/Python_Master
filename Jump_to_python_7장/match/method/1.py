import re
p = re.compile('[a-z]+')
m = p.match("python")

print(m.group())
print(m.start())
print(m.end())
print(m.span())