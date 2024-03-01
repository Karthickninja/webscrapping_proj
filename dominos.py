#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas
from bs4 import BeautifulSoup


# In[3]:


request=requests.get("https://www.dominos.co.in/store-location/chennai")
request


# In[4]:


request.content


# In[6]:


soup=BeautifulSoup(request.content,"html.parser")
soup


# In[8]:


Location=soup.find_all("p" ,{"class":"city-main-sub-title"})
Location


# In[9]:


for i in Location:
    print(i.text)


# In[10]:


Location=[i.text for i in Location]
Location


# In[12]:


Address=soup.find_all("p" ,{"class":"grey-text mb-0"})
Address


# In[13]:


for i in Address:
    print(i.text)


# In[14]:


Address=[i.text for i in Address]
Address


# In[20]:


Timing=soup.find_all("div", {"class":"col-xs-9 col-md-9 pl0 search-grid-right-text"})
Timing


# In[24]:


for i in Timing:
    print((i.text).strip())


# In[29]:


Timings=[i.text .strip("\t\n") for i in Timing]
Timings


# In[34]:


len(Location),len(Address),len(Timings)


# In[37]:


showcase={"Location":Location,"Address":Address,"Timings":Timings}
showcase


# In[39]:


view=pandas.DataFrame(showcase)
view


# In[46]:


view.to_csv("Dominos.csv")

