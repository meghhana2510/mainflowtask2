#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


df = pd.read_excel("C:/Users/DELL/Downloads/orders.xlsx")

# Display the first few rows of the dataframe
print("Initial Data:")
print(df.head())


# In[ ]:





# In[5]:


data=df.copy


# In[10]:


x = [feature for feature in df.columns if df[feature].isnull().sum() > 1]

print("\nColumns with more than one missing value:")
print(x)


# In[11]:


data= df.dropna()


# In[13]:


print(data.head(2))


# In[14]:


data = data.drop_duplicates()


# In[17]:


#filtering
data = data[data['sales_qty'] > 50]
data.head()


# In[18]:


#sorting
data = data.sort_values(by='order_date')


# In[21]:


#summary
print(data.describe())


# In[ ]:




