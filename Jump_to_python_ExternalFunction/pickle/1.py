# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여줌

import pickle
f = open("again.txt", 'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data, f)
f.close() 
