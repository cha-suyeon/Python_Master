# return의 또 다른 쓰임새

def say_nick(nick):
    if nick == '바보':
        return
    print("나의 별명은 %s 입니다." % nick)

print(say_nick('야호'))
print(say_nick('바보'))
print(say_nick('멍청이'))

# 만약에 '바보'라는 값이 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나갑니다.
# 위의 예시도 결괏값은 없다. 수행할 문장만 있을 뿐!