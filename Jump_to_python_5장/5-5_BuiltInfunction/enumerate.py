# enumerate, 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# 보통 for과 함께 많이 쓰며, 굉장히 많이 보았던 함수인데 기능을 처음 알았다.
# for문에서 함께 쓰면 자료형의 현재 순서, 인덱스 값을 쉽게 알 수 있다.