#!/usr/bin/env python
# coding: utf-8

# ## 문자열 포매팅

# In[4]:


# 숫자 바로 대입
print("I eat %d apples." % 3)


# In[5]:


# 문자열 바로 대입
print("I eat %s apples." % "five")


# In[6]:


# 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)


# In[7]:


# 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))


# In[8]:


# 문자열 포맷 코드

# %s : 문자열(string)
# %c : 문자 1개(Character)
# %d : 정수 (interger)
# %f : 부동 소수(Floating-point)
# %o : 8진수
# %x : 16진수
# %% : Literal % (문자 '%' 자체)


# In[9]:


# %s format 코드 : 뒤를 무조건 문자열로 바꿔준다.
print("I have %s apples." % 3)
print("rate is %s" % 3.234)


# In[10]:


# 포맷 코드와 숫자 함께 사용하기
# 정렬과 공백
print("%10s" % "hi")


# - %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 나머지는 공백으로 남겨둠

# In[11]:


print("%-10sjane" % "hi")


# - hi를 왼쪽에 정렬하고, 나머지는 공백을 채운 뒤 jane이 나온다.

# In[12]:


# 소수점 표현하기
print("%0.4f" % 3.42123234)


# In[13]:


print("%10.4f" % 3.42123234)


# In[14]:


# format 함수를 사용한 포매팅
# 숫자 바로 대입하기
print("I eat {0} apples".format(3))


# In[15]:


# 문자열 바로 대입하기
print("I eat {0} apples".format("five"))


# In[16]:


# 숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples".format(number))


# In[17]:


# 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))


# - 2개 이상의 값을 넣을 경우 {0}, {1} 과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다.

# In[18]:


# 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days".format(number=10, day=3))


# In[19]:


# 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
# name = value 형태도 가능


# In[20]:


# 왼쪽 정렬
print("{0:<10}".format("hi"))


# In[23]:


# 오른쪽 정렬
print("{0:>10}".format("hi"))


# In[24]:


# 가운데 정렬
print("{0:^10}".format("hi"))


# In[25]:


# 공백 채우기
print("{0:=^10}".format("hi"))


# In[26]:


print("{0:!^10}".format("hi"))


# In[27]:


# 소수점 표현하기
y = 3.42123234
print("{0:0.4f}".format(y))


# In[29]:


# 왼쪽 공백 두고 소수점 표현하기
print("{0:10.4f}".format(y))


# In[30]:


# {또는} 문자 표현하기
print("{{and}}".format())


# In[31]:


# f 문자 포매팅
name = "차수연"
age = 25
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')


# In[32]:


print(f'나는 내년이면 {age+1}살이 된다.')


# In[37]:


# 딕셔너리에서 f 사용
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')


# In[38]:


# 딕셔너리 정렬
print(f'{"hi":<10}') # 왼쪽 정렬
print(f'{"hi":>10}') # 오른쪽 정렬
print(f'{"hi":^10}') # 가운데 정렬


# In[39]:


# 딕셔너리 공백 채우기
print(f'{"hi":=^10}')
print(f'{"hi":!^10}')


# In[40]:


# 딕셔너리 소수점
print(f'{y:0.4f}')
print(f'{y:10.4f}')


# In[41]:


# f 문자열에서 {} 표현
print(f'{{ and }}')


# In[45]:


# '!!!python!!!' 문자열을 출력해보자
print(f'{"python":!^12}')


# In[46]:


print("{0:!^12}".format('python'))


# ## 문자열 관련 함수

# In[47]:


# 문자 개수 세기(count)
a = "hobby"
print(a.count('b'))


# In[48]:


# 위치 알려주기 1(find)
a = "Python is the best choice"
print(a.find('b'))


# In[49]:


# 존재하지 않는 문자열은 -1 로 반환
print(a.find('x'))


# In[50]:


# 위치 알려주기 2(index)
a = "Life is too short"
print(a.index('t'))


# In[51]:


# k가 없기 때문에 오류 발생
print(a.index('k'))


# In[52]:


# 문자열 삽입 (join)
print(",".join('abcd'))


# - abcd 문자열의 각각의 문자 사이에 ','를 삽입한다. join은 문자열 뿐만 아니라 리스트나 튜플도 입력으로 사용 가능하다.

# In[53]:


# 소문자를 대문자로 바꾸기 (upper)
a = "hi"
print(a.upper())


# In[54]:


# 대문자를 소문자로 바꾸기 (lower)
a = "HI"
print(a.lower())


# In[55]:


# 왼쪽 공백 지우기 (lstrip)
a = " hi "
print(a.lstrip())


# In[57]:


# 오른쪽 공백 지우기 (rstrip)
print(a.rstrip())


# In[58]:


# 양쪽 공백 지우기
print(a.strip())


# In[60]:


# 문자열 바꾸기 (replace)
a = "Life is too short..."

print(a.replace("Life", "Your leg"))


# In[61]:


# 문자열 나누기 (split)
a = "Life is too short"
print(a.split()) # 공백을 기준으로 문자열 나눔


# In[62]:


b = "a:b:c:d"
print(b.split(':')) # : 기호를 기준으로 문자열 나눔


# split 함수는 괄호 안에 아무 것도 넣어주지 않으면 공백(스페이스, 탭, 엔더 등)을 기준으로 문자열을 나눠준다. b.split(":") 처럼 괄호 안에 값을 입력해주면 그 값을 기준으로 문자열을 나눠준다.
