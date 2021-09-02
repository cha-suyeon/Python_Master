# with 문과 함께 사용하기

f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

# 파일을 open했다면 close도 해주는 것이 좋다
# 하지만 이것도 귀찮은 사람들을 위해 자동 처리하기 위해 with이 생겼다.

with open("foo.txt", "w") as f: # txt파일을 f로 연다
    f.write("Life is too long, I don't need python") # 파일 안에 해당 값을 쓴다.

# with문을 사용하면 with문을 벗어나는 순간 열린 파일 객체 f가 자동으로 close 된다고 합니다.
