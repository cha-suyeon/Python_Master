# if __name__ == '__main__': 의 의미

# module_4 수정

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

if __name__ == "__main__":
    print(add(1,4))
    print(sub(4,1))

# if __name__ = "__main__"을 사용하면 module_4처럼 직접 이 파일을 시행했을 때
# 위의 조건문이 참이 되어 if문 다음 문장을 수행한다.
# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러 사용할 때는
# 위 조건문이 거짓이 되어 if문 다음 문장이 시행되지 않음.

