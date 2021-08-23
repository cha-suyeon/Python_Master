#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 6001
print('Hello')


# In[2]:


# 6002
print("Hello World")


# In[3]:


# 6003
print("Hello\nWorld")


# In[4]:


# 6004
print("\'Hello\'")


# In[5]:


# 6005
print('"Hello World"')


# In[6]:


# 6006
print("\"!@#$%^&*()\'")


# In[7]:


# 6007
print("\"C:\Download\\'hello\'.py\"")


# In[8]:


# 6008
print("print(\"Hello\\nWorld\")")


# In[9]:


# 6009
a = input()
print(a)


# In[12]:


# 6010
a = int(input())
print(a)


# In[13]:


# 6011
a = float(input())
print(a)


# In[14]:


# 6012
a = int(input())
b = int(input())
print(a,b,sep='\n')


# In[15]:


# 6013
a = input()
b = input()
print(b, a, sep='\n')


# In[16]:


# 6014
a = float(input())
for i in range(3):
    print(a)


# In[21]:


# 6015
a, b = input().split()
print(a,b,sep='\n')


# In[22]:


# 6016
a, b = map(str, input().split())
print(b,a)


# In[23]:


# 6017
s = input()
print((s+' ')*3)


# In[25]:


# 6018
a, b = input().split(':')
print(a, b, sep=':')


# In[26]:


# 6019
y, m, d = input().split('.')
print(d, m, y, sep='-')


# In[27]:


# 6020
a,b=input().split('-')
print(a,b,sep="")


# In[28]:


# 6021
a = input()
for i in a:
    print(i)


# In[29]:


# 6022
a = input()
print(a[0:2], a[2:4], a[4:])


# In[30]:


# 6023
h, m, s = input().split(':')
print(m)


# In[31]:


# 6024
a, b = input().split()
print(a+b)


# In[1]:


# 6025
a = input()
b = input()
print(a+b)


# In[2]:


# 6026
a, b = map(float, input().split())
print(a+b)


# In[4]:


# 6027
print('%x' %int(input()))


# In[5]:


# 6028
print('%X' %int(input()))


# In[6]:


# 6029
print('%o' %int(input(),16))

# a = input()
# n = int(a, 16)
#입력된 a를 16진수로 인식해 변수 n에 저장
# print('%o' % n)
# n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력


# In[8]:


# 6030
print(ord(input()))


# In[9]:


# 6031
print(chr(int(input())))


# In[10]:


# 6032
print(-int(input()))


# In[11]:


# 6033
print(chr(ord(input())+1))

