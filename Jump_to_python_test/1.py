# Q1 문자열 바꾸기
# 문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오.
# a:b:c:d 👉 a#b#c#d

a = "a:b:c:d"
b = a.split(':')
print('#'.join(b))

a = "a:b:c:d"
b = a.replace(':', '#')
print(b)