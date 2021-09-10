# tempfile
# 파일을 임시로 만들어서 사용할 때
# tempfile.mkstemp() 중복되지 않는 임시 파일 이름을 무작위로 만들어서 돌려줌

import tempfile
filename = tempfile.mktemp()
print(filename)