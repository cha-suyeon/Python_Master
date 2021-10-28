# 키워드 파라미터 **

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name="foo", age=3)

# Wow!

# 출력값
# {'a': 1}
# {'name': 'foo', 'age': 3}

# 입력값 a=1, name="foo", age=3는 모두 딕셔너리로 만들어져서 출력된다.
# 즉, **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고
# key=value 형태의 결괏값이 그 딕셔너리에 저장된다.
# kwargs는 key arguments의 약자임
