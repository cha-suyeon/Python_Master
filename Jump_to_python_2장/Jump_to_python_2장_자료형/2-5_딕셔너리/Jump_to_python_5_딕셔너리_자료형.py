#!/usr/bin/env python
# coding: utf-8

# # 2-5 딕셔너리 자료형
# 
# 딕셔너리란?   
# 사람은 누구나 '이름'='홍길동', '생일'='몇 월 몇 일' 등으로 구별할 수 있다. 파이썬에도 이런 자료형이 있다. 대응 관계를 나타내는 자료형인데 이를 연관 배열(Association array) 또는 해시(Hash)라고 한다. 파이썬에서는 **딕셔너리(Dictionary)** 라고 하는데, 단어 그대로 해석하면 사전이라는 뜻이다. '야구'가 'baseball'인 것처럼 딕셔너리는 **key** 와 **value** 를 갖는다. 딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 key를 통해 valuse를 얻는다.

# In[1]:


# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
dic = {'name':'pey', 'phone':'01012345678', 'birth':'0830'}


# In[2]:


dic


# In[4]:


a = {1:'hi'}
a


# In[6]:


a = {'a':[1,2,3]}
a


# In[7]:


# 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b'
a


# In[8]:


a['name'] = 'pey'
a


# In[9]:


a[3] = [1,2,3]
a


# In[10]:


# 딕셔너리 요소 삭제하기
del a[1]
a


# del a[key]로 입력하면 {key:value} 쌍이 삭제된다.

# In[11]:


# 딕셔너리에서 key 사용해 value 얻기
grade = {'pey':10, 'juliet':90}
grade['pey']


# In[12]:


grade['juliet']


# In[13]:


a = {1:'a', 2:'b'}
print(a[1]) # key가 1인 요소의 value 반환
print(a[2]) # key가 2인 요소의 value 반환


# 리스트와 튜플의 다른 점은, 딕셔너리는 a[key]를 입력하면 key의 요소에 해당하는 value가 반환된다는 점이다. 리스트와 튜플은 인덱싱 방법에 사용되기 때문에 인덱스 값으로 입력된다.

# In[14]:


a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])


# In[15]:


dic = {'name':'pey', 'phone':'01012345678', 'birth':'0830'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])


# In[16]:


# 딕셔너리 만들 때 주의 사항
a = {1:'a', 1:'b'} # key 값이 중복
a


# # 딕셔너리 특징 및 주의 사항
# 
# ❗ 딕셔너리에 key는 고유값이어야 한다. 중복되는 key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다. 위에서 보듯이 동일한 key가 2개 존재할 경우 1:'a' 쌍이 무시된다.
# 
# ❗ 무시되는 이유는 key가 중복되었을 때 key를 통해서 value를 얻는 딕셔너리의 특징 때문인데, 동일한 key가 존재하면 어떤 key에 해당하는 value를 불러야 할 지 알 수 없기 때문이다.
# 
# ❗ 또 한 가지 주의 사항은 key에 리스트는 쓸 수 없다. 하지만 튜플은 가능하다. 딕셔너리에 key에 쓸 수 있는 값은 변하는 값인지, 변하지 않는 값인지에 따라 달려 있다. 리스트는 값이 변화하기 때문에 key로 쓸 수 없다.

# In[17]:


a = {[1,2] : 'hi'}


# In[18]:


# 딕셔너리 관련 함수
# Key 리스트 만들기(keys)
a = {'name':'pey', 'phone':'01012345678', 'birth':'0830'}
a.keys()


# In[19]:


# a.keys()는 딕셔너리 a의 Key만 모아서 dict_keys 객체를 돌려준다.
# dict_keys 객체는 리스트를 사용하는 것과 차이가 없다.
# append, insert, pop, remove, sort 함수는 수행할 수 없다.


# In[20]:


for k in a.keys():
    print(k)


# In[21]:


list(a.keys())


# In[22]:


# Value 리스트 만들기(values)
a.values()


# In[23]:


# value값을 얻는 것도 Key를 얻는 방법과 동일하다


# In[24]:


for k in a.values():
    print(k)


# In[25]:


list(a.values())


# In[26]:


# Key, Value 쌍 얻기(items)
a.items()


# In[27]:


# items() 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
# dict_values 객체와 dict_items 객체 역시 dict_keys 객체와 마찬가지로 리스트를 사용함


# In[28]:


# Key:Value 쌍 모두 지우고(clear)
a.clear()
a


# In[29]:


# Key로 Value 얻기(get)
a = {'name':'pey', 'phone':'01012345678', 'birth':'0830'}
a.get('name')


# In[30]:


a.get('birth')


# In[31]:


# get(x) 함수는 x라는 Key에 대응하는 Value를 돌려줍니다.
# a.get('name') = a['name']


# In[34]:


# None을 리턴
a.get('Birht')


# In[35]:


a.get('foo', 'bar')


# 딕셔너리 안에 찾으려는 Key 값이 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때 get(x, '디폴트 값')을 사용하면 편리하다.

# In[36]:


a =  {'name':'pey', 'phone':'01012345678', 'birth':'0830'}
'name' in a


# In[37]:


'email' in a


# 'name' 문자열은 a 딕셔너리의 Key 중 하나이다. 'name' in a 는  True를 돌려주고, 'email' in a 는 False를 돌려준다.
