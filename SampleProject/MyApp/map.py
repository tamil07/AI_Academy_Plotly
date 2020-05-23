#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import plotly.graph_objects as go


# In[7]:


df = pd.read_csv("time_series_covid_19_confirmed.csv")
df.head()


# In[9]:


df = df.rename(columns= {"Country/Region" : "Country", "Province/State": "Province"})
df.head()


# In[10]:


df['text'] = df['Country'] + " " + df["4/13/20"].astype(str)


# In[11]:


fig = go.Figure(data = go.Scattergeo(
    lon = df["Long"],
    lat = df["Lat"],
    text = df["text"],
    mode = "markers",
    marker = dict(
        size = 12,
        opacity = 0.8,
        reversescale = True,
        autocolorscale = True,
        symbol = 'square',
        line = dict(
            width = 1,
            color = 'rgba(102, 102, 102)'
        ),
        cmin = 0,
        color = df['4/13/20'],
        cmax = df['4/13/20'].max(),
        colorbar_title = "COVID 19 Reported Cases"
    )
))


# In[12]:


fig.update_layout(
    title = "COVID19 Confirmed Cases Around the World",
    geo = dict(
        scope = "world",
        showland = True,
    )
)


# In[13]:


fig.write_html('first_figure.html', auto_open=True)


# In[ ]:





