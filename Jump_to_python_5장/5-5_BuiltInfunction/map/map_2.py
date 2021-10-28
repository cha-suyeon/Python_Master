# map 으로 바꿔서 푸는 예제

def two_times(x): return x*2

print(list(map(two_times, [1,2,3,4]))) # [2, 4, 6, 8]

# 예제와 map으로 바꾼 예제의 차이가 무엇인가?
# map(f, iterable)이었던 것을 생각하면 map의 앞에 함수만 넣고, 뒤에는 반복 가능한 객체를 넣었다.
# 그리고 two_times라는 함수를 통해 객체는 2를 곱한 값이 출력된다.
# 이것을 lambda로 만들어본다면?


