#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
from plotly.colors import DEFAULT_PLOTLY_COLORS # plotly 기본 색상값


# In[3]:


# 서울 총 거주인구수 추이

df = pd.read_csv('c:/analysis/과제/서울 총 거주인구.csv', encoding = 'utf-8')

trace = go.Scatter(
    x = df['년도'],
    y = df['서울 총 인구수'],
    mode = 'markers + lines',
    marker = dict(size = 10)
)

data = [trace]
layout = go.Layout(title = '서울특별시 총 거주인구 수 변화',
                  xaxis = dict(title = '년도'),
                    yaxis = dict(title = '거주 인구 수'))
fig1 = go.Figure(data, layout)

fig1.show()


# In[4]:


# 서울 청년 거주인구수 추이

df2 = pd.read_csv('c:/analysis/과제/서울 거주인구 청년3.csv', encoding='utf-8')

# 여자와 남자 막대 생성
trace1 = go.Bar(x=df2['년도'], y=df2['여자'], name='청년 인구수-여자', offset=0, marker=dict(color='pink'), width =0.3)
trace2 = go.Bar(x=df2['년도'], y=df2['남자'], name='청년 인구수-남자', offset=0, marker=dict(color='blue'), width =0.3)

# 서울특별시 총인구 막대 생성
trace3 = go.Bar(x=df2['년도']+0.5, y=df2['서울특별시 총인구'], name='서울특별시 청년 거주 인구수', offset=0, marker=dict(color='grey'), width =0.3)

# 그래프 데이터 설정
data = [trace1, trace2, trace3]

# 그래프 레이아웃 설정
layout = go.Layout(
    title='서울특별시 청년(성별) 거주인구수 변화',
    xaxis=dict(title='년도'),
    yaxis=dict(title='청년 거주 인구 수'),
    barmode='stack'
)

# 그래프 생성
fig2 = go.Figure(data, layout)

# 그래프 표시
fig2.show()


# In[6]:


df3 = pd.read_csv('c:/analysis/과제/서울시 구별 청년인구.csv', encoding = 'utf-8')
trace1 = go.Bar(x = df3['구'], y = df3['2016'], name = '2016년')

trace2 = go.Bar(x = df3['구'], y = df3['2022'], name = '2022년')

data = [trace1, trace2]

layout = go.Layout(title = '서울특별시 구별 청년인구수 변화',
                   xaxis = dict(title = '구'),
                   yaxis = dict(title = '구별 청년인구수'),
                   barmode='group')

fig3 = go.Figure(data, layout)
fig3.show()


# In[7]:


#2016년 매매

df4 = pd.read_csv('c:/analysis/과제/아파트 매매 2016.csv', encoding = 'euc-kr', header=15)
df4['거래금액(만원)'] = df4['거래금액(만원)'].replace(',', '', regex=True).astype(float)


# In[17]:


df4


# In[8]:


df4_mean=df4['거래금액(만원)'].mean()


# In[9]:


df4_summary_시군구 = df4.groupby(by = '시군구', as_index=False).mean('거래금액(만원)')


# In[10]:


df4['구'] = df4['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)


# In[11]:


df4_summary_구 = df4.groupby(by = '구', as_index=False).mean('거래금액(만원)')


# In[12]:


count_per_구 = df4['구'].value_counts()


# In[13]:


print(df4_summary_구.columns)


# In[14]:


df4_summary_구 = pd.merge(df4_summary_구, count_per_구, left_on='구', right_index=True, how='left')


# In[15]:


df4_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
df4_summary_구.rename(columns={'구_x': '구'}, inplace=True)


# In[19]:


trace1 = go.Bar(x = df4_summary_구['구'], y = df4['2016'], name = '2016년')


data = [trace1]

layout = go.Layout(title = '서울특별시 구별 청년인구수 변화',
                   xaxis = dict(title = '구'),
                   yaxis = dict(title = '구별 청년인구수'),
                   barmode='group')

fig4 = go.Figure(data, layout)
fig4.show()


# In[ ]:





# In[ ]:





# In[15]:


# 2022년 매매가

df5 = pd.read_csv('c:/analysis/과제/아파트 매매 2022.csv', encoding = 'euc-kr', header=15)


# In[16]:


df5['거래금액(만원)'] = df5['거래금액(만원)'].replace(',', '', regex=True).astype(float)


# In[17]:


df5_mean=df5['거래금액(만원)'].mean()


# In[18]:


df5_summary_시군구 = df5.groupby(by = '시군구', as_index=False).mean('거래금액(만원)')


# In[19]:


df5['구'] = df5['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)


# In[20]:


df5_summary_구 = df5.groupby(by = '구', as_index=False).mean('거래금액(만원)')


# In[21]:


count_per_구_2022 = df5['구'].value_counts()


# In[22]:


print(df5_summary_구.columns)


# In[23]:


df5_summary_구 = pd.merge(df5_summary_구, count_per_구_2022, left_on='구', right_index=True, how='left')


# In[24]:


df5_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
df5_summary_구.rename(columns={'구_x': '구'}, inplace=True)


# In[ ]:





# In[26]:


# 매매가 변화 추이

import pandas as pd

#2016
sell2016 = pd.read_csv('c:/analysis/과제/아파트 매매 2016.csv', encoding = 'euc-kr', header=15)
sell2016

sell2016['거래금액(만원)'] = sell2016['거래금액(만원)'].replace(',', '', regex=True).astype(float)

sell2016_mean=sell2016['거래금액(만원)'].mean()
sell2016_mean



#2017
sell2017 = pd.read_csv('c:/analysis/과제/아파트(매매)__2017.csv', encoding = 'euc-kr', header=15)
sell2017

sell2017['거래금액(만원)'] = sell2017['거래금액(만원)'].replace(',', '', regex=True).astype(float)

sell2017_mean=sell2017['거래금액(만원)'].mean()
sell2017_mean


#2018
sell2018 = pd.read_csv('c:/analysis/과제/아파트(매매)__2018.csv', encoding = 'euc-kr', header=15)
sell2018

sell2018['거래금액(만원)'] = sell2018['거래금액(만원)'].replace(',', '', regex=True).astype(float)

sell2018_mean=sell2018['거래금액(만원)'].mean()
sell2018_mean


#2019
sell2019 = pd.read_csv('c:/analysis/과제/아파트(매매)__2019.csv', encoding = 'euc-kr', header=15)
sell2019

sell2019['거래금액(만원)'] = sell2019['거래금액(만원)'].replace(',', '', regex=True).astype(float)

sell2019_mean=sell2019['거래금액(만원)'].mean()
sell2019_mean


#2020
sell2020 = pd.read_csv('c:/analysis/과제/아파트(매매)__2020.csv', encoding = 'euc-kr', header=15)
sell2020

sell2020['거래금액(만원)'] = sell2020['거래금액(만원)'].replace(',', '', regex=True).astype(float)

sell2020_mean=sell2020['거래금액(만원)'].mean()
sell2020_mean


#2021
sell2021 = pd.read_csv('c:/analysis/과제/아파트(매매)__2021.csv', encoding = 'euc-kr', header=15)
sell2021

sell2021['거래금액(만원)'] = sell2021['거래금액(만원)'].replace(',', '', regex=True).astype(float)

sell2021_mean=sell2021['거래금액(만원)'].mean()
sell2021_mean


#2022
sell2022 = pd.read_csv('c:/analysis/과제/아파트 매매 2022.csv', encoding = 'euc-kr', header=15)
sell2022

sell2022['거래금액(만원)'] = sell2022['거래금액(만원)'].replace(',', '', regex=True).astype(float)

sell2022_mean=sell2022['거래금액(만원)'].mean()
sell2022_mean


# In[27]:


sell_mean = pd.DataFrame({'년도' : [2016,2017,2018,2019,2020,2021,2022],
                     '평균 거래가격' : [ sell2016_mean, sell2017_mean, sell2018_mean, sell2019_mean, sell2020_mean, sell2021_mean, sell2022_mean]})
sell_mean


# In[28]:


traces = []

traces.append(go.Scatter(x = sell_mean['년도'],
                              y = sell_mean['평균 거래가격'],
                              mode = 'lines + markers',
                              marker = dict(size = 10)
                            ))

data = traces

layout = go.Layout(title = '서울특별시 평균 매매가 변화',
                    xaxis = dict(title = '년도'),
                    yaxis = dict(title = '평균 거래가격'))

line__매매 = go.Figure(data, layout)
line__매매.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[29]:


#전월세

import pandas as pd
df6 = pd.read_csv('c:/analysis/과제/아파트 전월세 2016.csv', encoding = 'euc-kr', header=15)
df7 = pd.read_csv('c:/analysis/과제/아파트 전월세 2022.csv', encoding = 'euc-kr', header=15)


# In[30]:


df6_월세 = df6[df6['전월세구분'] == '월세']
df6_전세 = df6[df6['전월세구분'] == '전세']


# In[31]:


df7_월세 = df7[df7['전월세구분'] == '월세']
df7_전세 = df7[df7['전월세구분'] == '전세']


# In[32]:


df6_월세['월세(만원)'] = df6_월세['월세(만원)'].replace(',', '', regex=True).astype(float)

월세2016_mean2=df6_월세['월세(만원)'].mean()
월세2016_mean2


# In[33]:


df6_전세['보증금(만원)'] = df6_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)

전세2016_mean=df6_전세['보증금(만원)'].mean()
전세2016_mean


# In[34]:


df7_월세['월세(만원)'] = df7_월세['월세(만원)'].replace(',', '', regex=True).astype(float)

월세2022_mean2=df7_월세['월세(만원)'].mean()
월세2022_mean2


# In[35]:


df7_전세['보증금(만원)'] = df7_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)

전세2022_mean=df7_전세['보증금(만원)'].mean()
전세2022_mean


# In[ ]:





# In[36]:


df6_월세['구'] = df6_월세['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

월세2016_summary_구 = df6_월세.groupby(by = '구', as_index=False).mean('월세(만원)')


# In[37]:


count_per_구_월세2016 = df6_월세['구'].value_counts()


# In[38]:


월세2016_summary_구 = pd.merge(월세2016_summary_구, count_per_구_월세2016, left_on='구', right_index=True, how='left')


# In[39]:


월세2016_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
월세2016_summary_구.rename(columns={'구_x': '구'}, inplace=True)


# In[41]:


df6_전세['구'] = df6_전세['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

전세2016_summary_구 = df6_전세.groupby(by = '구', as_index=False).mean('보증금(만원)')

count_per_구_전세2016 = df6_전세['구'].value_counts()

전세2016_summary_구 = pd.merge(전세2016_summary_구, count_per_구_전세2016, left_on='구', right_index=True, how='left')

전세2016_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
전세2016_summary_구.rename(columns={'구_x': '구'}, inplace=True)


# In[43]:


df7_월세['구'] = df7_월세['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

월세2022_summary_구 = df7_월세.groupby(by = '구', as_index=False).mean('월세(만원)')

count_per_구_월세2022 = df7_월세['구'].value_counts()

월세2022_summary_구 = pd.merge(월세2022_summary_구, count_per_구_월세2022, left_on='구', right_index=True, how='left')

월세2022_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
월세2022_summary_구.rename(columns={'구_x': '구'}, inplace=True)


# In[45]:


df7_전세['구'] = df7_전세['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

전세2022_summary_구 = df7_전세.groupby(by = '구', as_index=False).mean('보증금(만원)')

count_per_구_전세2022 = df7_전세['구'].value_counts()

전세2022_summary_구 = pd.merge(전세2022_summary_구, count_per_구_전세2022, left_on='구', right_index=True, how='left')

전세2022_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
전세2022_summary_구.rename(columns={'구_x': '구'}, inplace=True)
전세2022_summary_구


# In[ ]:





# In[ ]:





# In[ ]:





# In[47]:


#전월세 변화 추이


# In[48]:


import pandas as pd
ws2016 = pd.read_csv('c:/analysis/과제/아파트 전월세 2016.csv', encoding = 'euc-kr', header=15)
ws2016_월세 = ws2016[ws2016['전월세구분'] == '월세']
ws2016_전세 = ws2016[ws2016['전월세구분'] == '전세']


# In[49]:


ws2016_월세['월세(만원)'] = ws2016_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2016_월세_mean=ws2016_월세['월세(만원)'].mean()


# In[50]:


ws2016_전세['보증금(만원)'] = ws2016_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2016_전세_mean=ws2016_전세['보증금(만원)'].mean()


# In[51]:


ws2017 = pd.read_csv('c:/analysis/과제/아파트 전월세 2017.csv', encoding = 'euc-kr', header=15)
ws2017_월세 = ws2017[ws2017['전월세구분'] == '월세']
ws2017_전세 = ws2017[ws2017['전월세구분'] == '전세']


# In[52]:


ws2017_월세['월세(만원)'] = ws2017_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2017_월세_mean=ws2017_월세['월세(만원)'].mean()


# In[53]:


ws2017_전세['보증금(만원)'] = ws2017_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2017_전세_mean=ws2017_전세['보증금(만원)'].mean()


# In[54]:


ws2018 = pd.read_csv('c:/analysis/과제/아파트 전월세 2018.csv', encoding = 'euc-kr', header=15)
ws2018_월세 = ws2018[ws2018['전월세구분'] == '월세']
ws2018_전세 = ws2018[ws2018['전월세구분'] == '전세']


# In[55]:


ws2018_월세['월세(만원)'] = ws2018_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2018_월세_mean=ws2018_월세['월세(만원)'].mean()


# In[56]:


ws2018_전세['보증금(만원)'] = ws2018_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2018_전세_mean=ws2018_전세['보증금(만원)'].mean()


# In[57]:


ws2019 = pd.read_csv('c:/analysis/과제/아파트 전월세 2019.csv', encoding = 'euc-kr', header=15)
ws2019_월세 = ws2019[ws2019['전월세구분'] == '월세']
ws2019_전세 = ws2019[ws2019['전월세구분'] == '전세']


# In[58]:


ws2019_월세['월세(만원)'] = ws2019_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2019_월세_mean=ws2019_월세['월세(만원)'].mean()


# In[59]:


ws2019_전세['보증금(만원)'] = ws2019_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2019_전세_mean=ws2019_전세['보증금(만원)'].mean()


# In[60]:


ws2020 = pd.read_csv('c:/analysis/과제/아파트 전월세 2020.csv', encoding = 'euc-kr', header=15)
ws2020_월세 = ws2020[ws2020['전월세구분'] == '월세']
ws2020_전세 = ws2020[ws2020['전월세구분'] == '전세']


# In[61]:


ws2020_월세['월세(만원)'] = ws2020_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2020_월세_mean=ws2020_월세['월세(만원)'].mean()


# In[62]:


ws2020_전세['보증금(만원)'] = ws2020_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2020_전세_mean=ws2020_전세['보증금(만원)'].mean()


# In[63]:


ws2021 = pd.read_csv('c:/analysis/과제/아파트 전월세 2021.csv', encoding = 'euc-kr', header=15)
ws2021_월세 = ws2021[ws2021['전월세구분'] == '월세']
ws2021_전세 = ws2021[ws2021['전월세구분'] == '전세']


# In[64]:


ws2021_월세['월세(만원)'] = ws2021_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2021_월세_mean=ws2021_월세['월세(만원)'].mean()


# In[65]:


ws2021_전세['보증금(만원)'] = ws2021_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2021_전세_mean=ws2021_전세['보증금(만원)'].mean()


# In[66]:


ws2022 = pd.read_csv('c:/analysis/과제/아파트 전월세 2022.csv', encoding = 'euc-kr', header=15)
ws2022_월세 = ws2022[ws2022['전월세구분'] == '월세']
ws2022_전세 = ws2022[ws2022['전월세구분'] == '전세']


# In[67]:


ws2022_월세['월세(만원)'] = ws2022_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2022_월세_mean=ws2022_월세['월세(만원)'].mean()


# In[68]:


ws2022_전세['보증금(만원)'] = ws2022_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2022_전세_mean=ws2022_전세['보증금(만원)'].mean()


# In[69]:


ws_mean_월세 = pd.DataFrame({'년도' : [2016,2017,2018,2019,2020,2021,2022],
                     '평균 거래가격' : [ ws2016_월세_mean, ws2017_월세_mean, ws2018_월세_mean, ws2019_월세_mean, ws2020_월세_mean, ws2021_월세_mean, ws2022_월세_mean]})
ws_mean_월세


# In[70]:


ws_mean_전세 = pd.DataFrame({'년도' : [2016,2017,2018,2019,2020,2021,2022],
                     '평균 거래가격' : [ ws2016_전세_mean, ws2017_전세_mean, ws2018_전세_mean, ws2019_전세_mean, ws2020_전세_mean, ws2021_전세_mean, ws2022_전세_mean]})
ws_mean_전세


# In[71]:


import plotly.graph_objects as go

traces = []

traces.append(go.Scatter(x = ws_mean_월세['년도'],
                              y = ws_mean_월세['평균 거래가격'],
                              mode = 'lines + markers',
                              marker = dict(size = 10)
                            ))

data = traces

layout = go.Layout(title = '서울특별시 평균 월세가 변화',
                    xaxis = dict(title = '년도'),
                    yaxis = dict(title = '평균 거래가격'))

line_월세 = go.Figure(data, layout)
line_월세.show()


# In[72]:


import plotly.graph_objects as go

traces = []

traces.append(go.Scatter(x = ws_mean_전세['년도'],
                              y = ws_mean_전세['평균 거래가격'],
                              mode = 'lines + markers',
                              marker = dict(size = 10)
                            ))

data = traces

layout = go.Layout(title = '서울특별시 평균 전세가 변화',
                    xaxis = dict(title = '년도'),
                    yaxis = dict(title = '평균 거래가격'))

line_전세 = go.Figure(data, layout)
line_전세.show()


# In[ ]:





# In[ ]:





# In[73]:


#지도 만들기(매매)


# In[74]:


df4_summary_구.rename(columns={'거래금액(만원)': '평균거래금액(만원)_2016'}, inplace=True)
df4_summary_구


# In[75]:


df5_summary_구.rename(columns={'거래금액(만원)': '평균거래금액(만원)_2022'}, inplace=True)
df5_summary_구


# In[76]:


merged_df = pd.merge(df4_summary_구, df5_summary_구, on='구')
merged_df

average_prices = merged_df.groupby('구')[['평균거래금액(만원)_2016', '평균거래금액(만원)_2022']].mean()
average_prices

average_prices['거래금액증감(만원)'] = average_prices['평균거래금액(만원)_2022'] - average_prices['평균거래금액(만원)_2016']
average_prices


# In[ ]:





# In[77]:


import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

seoul = gpd.read_file('c:/analysis/과제/LARD_ADM_SECT_SGG_11.shp', encoding = 'euc-kr')
seoul.explore()


# In[78]:


seoul.rename(columns={'SGG_NM': '구'}, inplace=True)
seoul


# In[79]:


sell_map = pd.merge(seoul, average_prices, left_on='구', right_index=True, how='left')
sell_map 


# In[80]:


map1=sell_map.explore(cmap = 'YlOrRd',column = '거래금액증감(만원)')
map1


# In[ ]:





# In[81]:


import plotly.express as px
import geopandas as gpd

map1 = sell_map.set_index('구').to_crs(4326)

fig200 = px.choropleth_mapbox( map1,
                           geojson = map1.geometry,
                           locations =  map1.index,
                           color =  map1['거래금액증감(만원)'],
                           mapbox_style = 'carto-positron',
                           color_continuous_scale = "YlOrRd",
                           zoom = 8.5, center = {"lat": 37.6, "lon": 127})

fig200.update_layout(title = '서울특별시 구별 매매가 증가율')

fig200.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[82]:


########### 지도 만들기 -월세


# In[83]:


월세2016_summary_구.rename(columns={'월세(만원)': '평균월세금액(만원)_2016'}, inplace=True)
월세2016_summary_구


# In[84]:


월세2022_summary_구.rename(columns={'월세(만원)': '평균월세금액(만원)_2022'}, inplace=True)
월세2022_summary_구


# In[85]:


merged_df_월세 = pd.merge(월세2016_summary_구, 월세2022_summary_구, on='구')
merged_df_월세

average_prices_월세 = merged_df_월세.groupby('구')[['평균월세금액(만원)_2016', '평균월세금액(만원)_2022']].mean()
average_prices_월세

average_prices_월세['월세 증감(만원)'] = average_prices_월세['평균월세금액(만원)_2022'] - average_prices_월세['평균월세금액(만원)_2016']
average_prices_월세


# In[86]:


월세_map = pd.merge(seoul, average_prices_월세, left_on='구', right_index=True, how='left')
월세_map 


# In[87]:


map2=월세_map.explore(cmap = 'YlOrRd',column = '월세 증감(만원)')
map2


# In[88]:


import plotly.express as px
import geopandas as gpd

map2 = 월세_map.set_index('구').to_crs(4326)

fig_월세map = px.choropleth_mapbox( map2,
                           geojson = map2.geometry,
                           locations =  map2.index,
                           color =  map2['월세 증감(만원)'],
                           mapbox_style = 'carto-positron',
                           color_continuous_scale = "YlOrRd",
                           zoom = 8.5, center = {"lat": 37.6, "lon": 127})

fig_월세map.update_layout(title = '서울특별시 구별 월세 증가율')

fig_월세map.show()


# In[ ]:





# In[ ]:





# In[89]:


################지도 만들기-전세


# In[90]:


전세2016_summary_구


# In[91]:


전세2016_summary_구.rename(columns={'보증금(만원)': '평균보증금액(만원)_2016'}, inplace=True)
전세2016_summary_구


# In[92]:


전세2022_summary_구.rename(columns={'보증금(만원)': '평균보증금액(만원)_2022'}, inplace=True)
전세2022_summary_구


# In[93]:


merged_df_전세 = pd.merge(전세2016_summary_구, 전세2022_summary_구, on='구')
merged_df_전세

average_prices_전세 = merged_df_전세.groupby('구')[['평균보증금액(만원)_2016', '평균보증금액(만원)_2022']].mean()
average_prices_전세

average_prices_전세['보증금 증감(만원)'] = average_prices_전세['평균보증금액(만원)_2022'] - average_prices_전세['평균보증금액(만원)_2016']
average_prices_전세


# In[94]:


전세_map = pd.merge(seoul, average_prices_전세, left_on='구', right_index=True, how='left')
전세_map 


# In[95]:


map3=전세_map.explore(cmap = 'YlOrRd',column = '보증금 증감(만원)')
map3


# In[96]:


import plotly.express as px
import geopandas as gpd

map3 = 전세_map.set_index('구').to_crs(4326)

fig_전세map = px.choropleth_mapbox( map3,
                           geojson = map3.geometry,
                           locations =  map3.index,
                           color =  map3['보증금 증감(만원)'],
                           mapbox_style = 'carto-positron',
                           color_continuous_scale = "YlOrRd",
                           zoom = 8.5, center = {"lat": 37.6, "lon": 127})

fig_전세map.update_layout(title = '서울특별시 구별 전세 보증금 증가율')

fig_전세map.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[97]:


############# 지도 만들기 - 청년 인구


# In[98]:


pop = pd.read_csv('c:/analysis/과제/서울시 구별 청년인구.csv', encoding = 'utf-8')
pop['2016'].dtype

seoul['구'].dtype

pop['구'] = pop['구'].astype(str)

pop['구'].dtype

seoul['구'] = seoul['구'].astype(str)
pop['구'] = pop['구'].astype(str)

print(pop.index.dtype)


# In[99]:


pop.index = pop.index.astype(str)

pop_map = pd.merge(seoul, pop, left_on='구', right_index=True, how='left')
pop_map

print(set(seoul['구'].unique()) - set(pop['구'].unique()))

seoul['구'] = seoul['구'].str.strip().str.lower()
pop['구'] = pop['구'].str.strip().str.lower()

pop_map = pd.merge(seoul, pop, on='구', how='left')
pop_map


# In[100]:


pop_map['청년 인구 증감'] = pop_map['2016'] - pop_map['2022']
pop_map


# In[101]:


pop_map.explore(cmap = 'PuBu',column = '청년 인구 증감')


# In[102]:


import plotly.express as px
import geopandas as gpd


pop_map1 = pop_map.set_index('구').to_crs(4326)

fig400 = px.choropleth_mapbox(pop_map1,
                               geojson=pop_map1.geometry,
                               locations=pop_map1.index,
                               color=pop_map1['청년 인구 증감'],
                               mapbox_style='carto-positron',
                               color_continuous_scale="PuBu",
                               zoom=8.5, center={"lat": 37.6, "lon": 127})

fig400.update_layout(title='서울특별시 구별 청년 인구 감소율')

fig400.show()


# In[ ]:





# In[ ]:





# In[103]:


#########주거 점유율


# In[104]:


apt = pd.read_csv('c:/analysis/과제/주거실태현황(주택유형,점유형태등)_2020.csv', encoding = 'utf-8', header =1)
apt

trace = go.Bar(
    x = apt['주거실태별(2)'],
    y = apt['서울'],
    ) 

data = [trace]

layout = go.Layout(title = '2020년 기준 서울특별시 주거 점유형태',
                  xaxis = dict(title = '주거 형태'),
                    yaxis = dict(title = '주거 점유율'))


fig_주거점유율 = go.Figure(data, layout)
fig_주거점유율.show()


# In[ ]:





# In[ ]:





# In[105]:


############# 출산율


# In[106]:


baby2016 = pd.read_csv('c:/analysis/과제/출산율 2016.csv', encoding = 'euc-kr', header =2)
baby2016_mean=baby2016['합계출산율'].mean()
baby2016_mean

baby2017 = pd.read_csv('c:/analysis/과제/출산율 2017.csv', encoding = 'euc-kr', header =2)
baby2017_mean=baby2017['합계출산율'].mean()
baby2017_mean

baby2018 = pd.read_csv('c:/analysis/과제/출산율 2018.csv', encoding = 'euc-kr', header =2)
baby2018_mean=baby2018['합계출산율'].mean()
baby2018_mean

baby2019 = pd.read_csv('c:/analysis/과제/출산율 2019.csv', encoding = 'euc-kr', header =2)
baby2019_mean=baby2019['합계출산율'].mean()
baby2019_mean

baby2020 = pd.read_csv('c:/analysis/과제/출산율 2020.csv', encoding = 'euc-kr', header =2)
baby2020_mean=baby2020['합계출산율'].mean()
baby2020_mean

baby2021 = pd.read_csv('c:/analysis/과제/출산율 2021.csv', encoding = 'euc-kr', header =2)
baby2021_mean=baby2021['합계출산율'].mean()
baby2021_mean

baby2022 = pd.read_csv('c:/analysis/과제/출산율 2022.csv', encoding = 'euc-kr', header =2)
baby2022_mean=baby2022['합계출산율'].mean()
baby2022_mean

baby = pd.DataFrame({'년도' : [2016,2017,2018,2019,2020,2021,2022],
                     '합계출산율' : [ baby2016_mean, baby2017_mean, baby2018_mean, baby2019_mean, baby2020_mean, baby2021_mean, baby2022_mean]})
baby


# In[107]:


#출산율 추이

traces = []

traces.append(go.Scatter(x = baby['년도'],
                              y = baby['합계출산율'],
                              mode = 'lines + markers',
                              marker = dict(size = 15)
                            ))

data = traces

layout = go.Layout(title = '서울특별시 합계출산율의 변화',
                    xaxis = dict(title = '년도'),
                    yaxis = dict(title = '합계출산율'))

fig_baby = go.Figure(data, layout)
fig_baby.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[108]:


import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
from plotly.colors import DEFAULT_PLOTLY_COLORS 


# In[34]:


import pandas as pd
from dash import Dash, dcc, html, Input, Output, State

app = Dash(__name__)
app.title = ('Dashboard | 서울특별시 부동산 상승과 인구 감소 사이의 관계')
server = app.server

app.layout = html.Div([
    html.H1('서울특별시 부동산 상승과 청년 인구 감소 간의 관계',
            style={'textAlign': 'center',
                   'marginBottom': 10,
                   'marginTop': 10}),
    html.Div([
    html.H3('#서울특별시 주거형태별 점유율',
            style={'textAlign': 'left',
                   'marginBottom': 10,
                   'marginTop': 10}),
        
    html.Div(className='Graph',
             children=[
                 html.Div(dcc.Graph(id='주택', figure=fig_주거점유율),
                          style={'float': 'left', 'display': 'inline-block', 'width': '100%'})])
             ]),
    
    
    html.Div([
    html.H3('#서울특별시 전체 아파트 부동산 변화와 인구수 변화',
            style={'textAlign': 'left',
                   'marginBottom': 10,
                   'marginTop': 10}),
    html.Div([
        html.Div(className='Graph',
                 children=[
                     html.Div(dcc.Graph(id='매매가격변화 추이', figure=line__매매),
                              style={'float': 'left', 'display': 'inline-block', 'width': '33%'}),
                     html.Div(dcc.Graph(id='월세가격변화 추이', figure=line_월세),
                              style={'float': 'left', 'display': 'inline-block', 'width': '33%'}),
                     html.Div(dcc.Graph(id='전세가격변화 추이', figure=line_전세),
                              style={'float': 'right', 'width': '33%'})])
                 ]),

        
        html.Div([
        html.H3('#서울특별시 구별 부동산 가격 변화와 청년 인구수 변화',
            style={'textAlign': 'left',
                   'marginBottom': 10,
                   'marginTop': 10}),
        html.Div(className='Graph',
                 children=[
                     html.Div(dcc.Graph(id='2016 매매', figure=fig4),
                              style={'float': 'left', 'display': 'inline-block', 'width': '50%'}),
                     html.Div(dcc.Graph(id='2022 매매', figure=fig5),
                              style={'float': 'right', 'display': 'inline-block', 'width': '50%'})
                 ]),

        html.Div(className='Graph',
                 children=[
                     html.Div(dcc.Graph(id='2016 월세', figure=월세_2016),
                              style={'float': 'left', 'display': 'inline-block', 'width': '50%'}),
                     html.Div(dcc.Graph(id='2022 월세', figure=월세_2022),
                              style={'float': 'right', 'display': 'inline-block', 'width': '50%'})
                 ]),

        html.Div(className='Graph',
                 children=[
                     html.Div(dcc.Graph(id='2016 전세', figure=전세_2016),
                              style={'float': 'left', 'display': 'inline-block', 'width': '50%'}),
                     html.Div(dcc.Graph(id='2022 전세', figure=전세_2022),
                              style={'float': 'right', 'display': 'inline-block', 'width': '50%'})])
                 ]),

        
        html.Div([
        html.H3('#서울특별시 구별 부동산 변화와 청년 인구수 변화 지도화',
            style={'textAlign': 'left',
                   'marginBottom': 10,
                   'marginTop': 10}),
        html.Div(className='map',
                 children=[
                     html.Div(dcc.Graph(id='매매 상승폭', figure=fig200),
                              style={'float': 'left', 'display': 'inline-block', 'width': '50%'}),
                     html.Div(dcc.Graph(id='월세 상승폭', figure=fig_월세map),
                              style={'float': 'right', 'display': 'inline-block', 'width': '50%'})
                 ]),

        html.Div(className='map',
                 children=[
                     html.Div(dcc.Graph(id='전세 상승폭', figure=fig_전세map),
                              style={'float': 'left', 'display': 'inline-block', 'width': '60%'})])
                 ]),
    ], style={'float': 'left', 'display': 'inline-block', 'width': '65%'}),

    html.Div([
        html.Div(className='Graph',
                 children=[
                     html.Div(dcc.Graph(id='서울시 총 인구', figure=fig1),
                              style={'float': 'left', 'display': 'inline-block', 'width': '100%', 'height': '700px'})
                 ]),

        html.Div(className='Graph',
                 children=[
                     html.Div(dcc.Graph(id='성별 인구', figure=fig2),
                              style={'float': 'left', 'display': 'inline-block', 'width': '100%', 'height': '500px'})
                 ]),

        html.Div(className='Graph',
                 children=[
                     html.Div(dcc.Graph(id='청년 인구', figure=fig3),
                              style={'float': 'left', 'display': 'inline-block', 'width': '100%', 'height': '700px'})
                 ]),

        html.Div(className='Graph',
                 children=[
                     html.Div(dcc.Graph(id='인구 하락-청년', figure=fig400),
                              style={'float': 'left', 'display': 'inline-block', 'width': '100%'}),
                 ]),
    ], style={'float': 'right', 'width': '35%'}),
    
    
    
    
     html.Div(className='Graph',
             children=[
                 html.Div(dcc.Graph(id='출산율', figure=fig_baby),
                          style={'float': 'left', 'display': 'inline-block', 'width': '100%'})
             ])
     

])

# run App
if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:





# In[ ]:




