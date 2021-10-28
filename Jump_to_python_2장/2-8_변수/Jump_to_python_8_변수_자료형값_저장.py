#!/usr/bin/env python
# coding: utf-8

# # 2-8 변수
# 
# 변수는 자료형의 값을 저장하는 공간이다.

# In[1]:


a = 1
b = "python"
c = [1,2,3]


# 위처럼 변수를 만들 때는,
# 
# > 변수 이름 = 변수에 저장할 값
# 
# 의 형식을 따르면 된다.
# 
# ## 변수란?
# 파이썬에서 사용하는 변수는 객체를 가리키는 말이다. 객체란 우리가 지금껏 보아 온 자료형과 같은 것을 의미하는 말이다.

# In[2]:


a = [1,2,3]


# 위처럼 변수를 지정하면 [1,2,3] 값을 가지는 리스트 자료형이 자동으로 메모리에 생성되고 변수 a는 [1,2,3]가 저장된 메모리의 주소를 얻게 됨

# In[3]:


# 저장된 주소 확인
id(a)


# ## 리스트를 복사할 때

# In[4]:


# 리스트를 복사할 때
a = [1,2,3]
b = a
b


# 👉 a와 b는 완전히 동일하다.
# a, b는 완전히 같은 리스트를 가졌다. 다만 [1,2,3]이라는 리스트를 참조하는 변수가 추가되었다는 차이가 있을 뿐이다.

# In[5]:


print(id(a))
print(id(b))


# a, b의 id 값이 동일하다. a가 가리키는 대상과 b가 가리키는 대상이 동일하다는 것을 알 수 있다. 동일한 객체를 가리키고 있는 지에 대해 판단하는 명령어 is를 사용하면

# In[6]:


a is b


# 참을 돌려준다.

# In[7]:


a[1] = 4
a


# In[8]:


b


# a 의 리스트 두 번째 요소를 4로 바꾸었더니 a만 바뀌는게 아니라 b도 바뀌었다. 이유는 a,b 모두 동일한 리스트를 가리키고 있기 때문. 그렇다면 b 변수를 생성할 때 a 변수의 값을 가져오면서 a와 다른 주소를 가리키도록 만드는 방법은 무엇일까?

# ## 1. [:] 사용

# In[12]:


a = [1,2,3]
b = a[:]
a[1] = 4
print(a)
print(b)


# In[13]:


print(id(a))
print(id(b))


# ## 2. copy 모듈 사용

# In[14]:


from copy import copy
a = [1,2,3]
b = copy(a)
print(a)
print(b)


# In[15]:


print(id(a))
print(id(b))


# In[16]:


# 'b = a[:]' = 'b = copy(a)'


# In[17]:


b is a


# ## 변수를 만드는 여러 가지 방법

# In[24]:


a, b = ('python', 'life')
print(a)
print(b)
print(a,b)


# In[25]:


(a, b) = ('python', 'life')
print(a)
print(b)
print(a,b)


# In[26]:


[a, b] = ['python', 'life']
print(a)
print(b)
print([a,b])


# In[27]:


a = b = ['python']
print(a)
print(b)


# In[28]:


a = 3
b = 5
a, b = b, a # a와 b의 값을 바꿈
print(a)
print(b)


# In[29]:


# 예제 - 실행 후 설명해보기
a = [1,2,3]
b = [1,2,3]
a is b


# a와 b는 서로 다른 메모리를 가지므로 False이다.
