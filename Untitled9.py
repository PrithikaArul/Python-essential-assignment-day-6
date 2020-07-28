#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Program to convert two lists into one dictionary using list comorehension method:
list1=[1,2,3,4,5,7,8]
list2=["a","b","c","d","e"]
len1=min(len(list1),len(list2))
dict1={}
print( [dict1[list1[each]] = list2[each]]  for each in range(len1))

