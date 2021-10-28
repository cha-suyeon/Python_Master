import re

p = re.compile('[a-z]', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))