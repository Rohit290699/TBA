#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = "Hello"
print(a)


# In[2]:


a = "Hello, World!"
print(a[1]) 
b = "Hello, World!"
print(b[2:5])


# In[3]:


a = "Hello, World!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("H", "J"))


# In[4]:


a = "HELLO"
b= "World"
c= a + " " + b 
print(c) 


# In[5]:


a = "Rohit Adike"

for ch in a:
    print(ch)


# In[6]:


quote = " Roses are not lillies"
quote[:]


# In[7]:


f1 = "Rose"
f2 = "lillies"
f1 in quote 


# In[8]:


f1 not in f2 


# In[9]:


quote.islower()


# In[10]:


myString="1 2 3 4 5"
print(myString.split())


# In[14]:


myString="1/2/3/4/5"
print(myString.split('/'))


# In[18]:


str = 'peach raspberry strawberry vanilla'
print(str.split())


# In[23]:


my_address = 'www.example.com/add'
print(my_address.split('.'))


# In[ ]:




