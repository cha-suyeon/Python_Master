import re
p = re.compile(r'\bclass\b')
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))
