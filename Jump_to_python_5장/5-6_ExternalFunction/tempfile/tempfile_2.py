# tempfile.TemporaryFile() 은 임시 저장 공간으로 사용할 파일 객체를 돌려줌
# 기본적으로 바이너리 쓰기 모드 wb 를 가짐
# f.close()가 호출되면 파일 객체는 자동으로 사라짐

import tempfile
f = tempfile.TemporaryFile()
f.close()