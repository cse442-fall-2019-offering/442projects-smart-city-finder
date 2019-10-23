#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import pandas as pd
import uuid
from random import choice


# In[57]:


names = np.array([str(uuid.uuid4()) for _ in range(1000)])
ages = np.random.randint(18, 31, (1000, ))
cities = np.array([choice(['NYC', 'Buffalo', 'SF', 'LA', 'Seattle', 'San Jose']) for _ in range(1000)])
transport = np.array([choice(['car', 'bike', 'bus', 'train']) for _ in range(1000)])
salary = np.random.randint(500, 15000, (1000, ))
height_cm = np.random.randint(100, 200, (1000, ))
weight_lb = np.random.randint(60, 400, (1000, ))
Job_Title = np.array([choice(['Software Enginner', 'Actor', 'Doctor', 'Teacher', 'Other']) for _ in range(1000)])
Shift_Hours = np.random.randint(20, 40, (1000, ))
df = pd.DataFrame()
df['id'] = names
df['age'] = ages
df['city'] = cities
df['transport'] = transport
df['salary'] = salary
df['height'] = height_cm
df['weight'] = weight_lb
df['job'] = Job_Title
df['shift hours'] = Shift_Hours

df.head()


# In[ ]:




