import re
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))