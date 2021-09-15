import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m) 