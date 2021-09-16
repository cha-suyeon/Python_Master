# 긍정적 전방 탐색

import re
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())