import re

p = re.compile('[a-z]+')
result = p.finditer("life is too short")
print(result)

for r in result:
    print(r)