# try ... finally

# try문에는 finally절을 사용할 수 있다. finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행됩니다.
# 보통 finally절은 사용한 리소스를 close 해야 할 때 많이 사용한다.


f = open('foo.txt', 'w')

try:
    # 무언가를 수행한다.
finally:
    f.close()

# foo.txt 파일을 쓰기 모드로 연 후에 try 문을 수행한 후 예외 발생 여부와 상관없이
# finally 절에서 f.close()로 닫을 수 있다.