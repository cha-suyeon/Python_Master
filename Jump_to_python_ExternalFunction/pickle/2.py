# pickle.dump로 저장한 파일을 pickle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 예
import pickle
f = open("again.txt", "rb")
data = pickle.load(f)
print(data)