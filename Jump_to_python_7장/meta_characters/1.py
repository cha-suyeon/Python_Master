# 7. 정규표현식

# 정규표현식은 복잡한 문자열을 처리할 때 사용하는 기법입니다.
# 파이썬만의 고유 문법이 아닌 문자열을 처리하는 모든 곳에서 사용된다.


# task: 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경해보자.

# 정규표현식 사용 전
data = """
park 800905-1049118
kim 700905-1059119
"""

# 결과를 담아줄 빈 리스트 생성
result = []

# 줄바꿈 되는 곳마다 split
for line in data.split('\n'):
    word_result = []
    # ' ' 공백마다 split
    for word in line.split(' '):
        # word의 길이가 14이면서, 앞 6자리와 뒤 7자리가 digit인 모든 조건을 만족하는
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            # word에 word에서 앞 6자리를 슬라이싱하여 '-'와 '*' 7개를 붙여준다.
            word = word[:6] + '-' + '*******'
        # for문 안에서 생성해둔 빈 리스트 word_result에 word 값을 담아준다.
        word_result.append(word)
    # result 에 word_result에 담긴 값을 ' ' 공백을 추가하여 담기
    result.append(' '.join(word_result))

# 다시 그 결과를 '\n' 줄 바꿈하여 출력
print('\n'.join(result))

# 결론: 복잡하다.

