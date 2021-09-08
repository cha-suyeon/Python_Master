# 예외 처리

# 오류는 어떨 때 발생하나요?
# 어떤 상황에서 어떤 오류가 발생하는지, 살펴보겠습니다.

f = open("없는 파일", 'r')

# 위 코드 시행시, 나타나는 에러는 아래와 같습니다.
# FileNotFoundError
# [Errno 2] No such file or directory: '없는 파일'
# 에러명이 'FileNotFoundError'인데요. 없는 파일을 열려고 시도했기 때문입니다.
