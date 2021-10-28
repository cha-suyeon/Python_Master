# subn

import re
# sub 매서드
p = re.compile('(blue|white|red)')

print(p.subn('colour', 'blue socks and red shoes'))