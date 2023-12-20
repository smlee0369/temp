#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
from plotly.colors import DEFAULT_PLOTLY_COLORS # plotly 기본 색상값


# In[ ]:





# In[2]:


######## 인구 파트 ##########


# In[3]:


#1.서울특별시 총 거주인구수 추이 그래프


# In[4]:


# 파일 읽기
df_data = pd.read_csv('c:/analysis/과제/서울 거주인구.csv', encoding = 'utf-8')
df_data


# In[5]:


# 필요한 부분 뽑고 행, 열 바꾸기
df_인구=df_data.loc[[0]]
df_인구

df_transposed = df_인구.transpose()
df_transposed_reset = df_transposed.reset_index()
df_transposed_reset


# In[6]:


# 다시 필요한 부분만 뽑고 열이름 바꾸기
df=df_transposed_reset.drop(df_transposed_reset.index[0:5])
df = df.rename(columns={'index': '년도', 0: '거주인구수'})
df


# In[7]:


# 서울 총 거주인구수 추이 그래프

trace = go.Scatter(
    x = df['년도'],
    y = df['거주인구수'],
    mode = 'markers + lines',
    marker = dict(size = 10)
)

data1 = [trace]
layout = go.Layout(title = '서울특별시 총 거주인구 수 변화',
                   xaxis = dict(title = '년도'),
                   yaxis = dict(title = '거주 인구수'))
fig1 = go.Figure(data1, layout)

fig1.show()


# In[8]:


#2. 서울특별시 성별 청년 인구수 그래프


# In[9]:


# 파일 읽기
df2 = pd.read_csv('c:/analysis/과제/서울 거주인구 청년.csv', encoding = 'utf-8')
df2


# In[10]:


# 여자, 남자, 총 청년 인구 각각 뽑기

df_여자 = df2[df2['성별'] == '여자']
df_남자 = df2[df2['성별'] == '남자']
df_계 = df2[df2['성별'] == '계']


# In[11]:


# 여자 청년인구수 데이터 정리

selected_columns = ['2016 년', '2017 년', '2018 년', '2019 년', '2020 년', '2021 년', '2022 년']

df_여자_int = df_여자[selected_columns].astype(float)

total_selected = df_여자_int[selected_columns].sum()

df_여자_reset = total_selected.reset_index()

여자=pd.DataFrame(df_여자_reset)

f_여자 = 여자.rename(columns={'index': '년도', 0: '청년 인구수_여자'})
f_여자


# In[12]:


# 남자 청년인구수 데이터 정리

df_남자_int = df_남자[selected_columns].astype(float)

total_selected2 = df_남자_int[selected_columns].sum()

df_남자_reset = total_selected2.reset_index()

남자=pd.DataFrame(df_남자_reset)

f_남자 = 남자.rename(columns={'index': '년도', 0: '청년 인구수_남자'})
f_남자


# In[13]:


# 서울특별시 총 청년인구수 데이터 정리

df_계_int = df_계[selected_columns].astype(float)

total_selected3 = df_계_int[selected_columns].sum()

df_계_reset = total_selected3.reset_index()

계=pd.DataFrame(df_계_reset)

f_계 = 계.rename(columns={'index': '년도', 0: '서울특별시 총 청년인구수'})
f_계


# In[14]:


# 원하는 그래프를 만들기 위해 년도 부분에서 '년'을 빼고 문자형을 실수형으로 바꾸기

f_여자['년도'] = f_여자['년도'].str.extract('(\d+)').astype(float)
f_남자['년도'] = f_남자['년도'].str.extract('(\d+)').astype(float)
f_계['년도'] = f_계['년도'].str.extract('(\d+)').astype(float)


# In[15]:


# 여자와 남자 막대 생성
trace1 = go.Bar(x=f_여자['년도'], y=f_여자['청년 인구수_여자'], name='청년 인구수-여자', offset=0, marker=dict(color='pink'), width =0.3)
trace2 = go.Bar(x=f_남자['년도'], y=f_남자['청년 인구수_남자'], name='청년 인구수-남자', offset=0, marker=dict(color='blue'), width =0.3)

# 서울특별시 총인구 막대 생성
trace3 = go.Bar(x=f_계['년도']+0.5, y=f_계['서울특별시 총 청년인구수'], name='서울특별시 청년 거주 인구수', offset=0, marker=dict(color='grey'), width =0.3)

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


# In[16]:


#3.자치구별 청년 인구수 구하기 


# In[17]:


# 파일 읽기
df3 = pd.read_csv('c:/analysis/과제/서울시 자치구별 연령별 인구.csv', encoding = 'utf-8')
df3


# In[18]:


# 팔요한 자료만 뽑기
df3=df3.drop(columns =['2017','2017.1','2017.2','2017.3','2018','2018.1','2018.2','2018.3','2019','2019.1','2019.2','2019.3','2020','2020.1','2020.2','2020.3','2021','2021.1','2021.2','2021.3'])
df3 =df3[df3['성별']=='계']
df3.drop(index=2, inplace=True)


# 2016년, 2022년 구별로 합하기
df3['2016년'] = pd.to_numeric(df3['2016']) + pd.to_numeric(df3['2016.1']) + pd.to_numeric(df3['2016.2']) + pd.to_numeric(df3['2016.3'])

df3['2022년'] = pd.to_numeric(df3['2022']) + pd.to_numeric(df3['2022.1']) + pd.to_numeric(df3['2022.2']) + pd.to_numeric(df3['2022.3'])

df3


# In[19]:


trace1 = go.Bar(x = df3['동별'], y = df3['2016년'], name = '2016년')

trace2 = go.Bar(x = df3['동별'], y = df3['2022년'], name = '2022년')

data = [trace1, trace2]

layout = go.Layout(title = '서울특별시 구별 청년인구수 변화',
                   xaxis = dict(title = '구'),
                   yaxis = dict(title = '구별 청년인구수'),
                   barmode='group')

fig3 = go.Figure(data, layout)
fig3.show()


# In[ ]:





# In[ ]:





# In[20]:


######## 부동산 파트 #########


# In[21]:


## 매매


# In[22]:


#1.2016년 매매


# In[23]:


# 자료 불러오기
df4 = pd.read_csv('c:/analysis/과제/아파트 매매 2016.csv', encoding = 'euc-kr', header=15)
df4


# In[24]:


# 거래금액 실수형으로 바꾸기
df4['거래금액(만원)'] = df4['거래금액(만원)'].replace(',', '', regex=True).astype(float)

# 매매 평균 가격 구하기
df4_mean=df4['거래금액(만원)'].mean()

# 시군구별로 그룹화하기
df4_summary_시군구 = df4.groupby(by = '시군구', as_index=False).mean('거래금액(만원)')

# 거래금액 평균으로 구별로 구룹화하기
df4['구'] = df4['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

df4_summary_구 = df4.groupby(by = '구', as_index=False).mean('거래금액(만원)')

# 각 구별 거래건수 구하기
count_per_구 = df4['구'].value_counts()

print(df4_summary_구.columns)


# In[25]:


# 구별로 요약한 자료와 구한 각 구별 거래건수 mergy
df4_summary_구 = pd.merge(df4_summary_구, count_per_구, left_on='구', right_index=True, how='left')
df4_summary_구


# In[26]:


# 열 이름 바꾸기

df4_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
df4_summary_구.rename(columns={'구_x': '구'}, inplace=True)
df4_summary_구


# In[ ]:





# In[27]:


#2. 2022년 매매


# In[28]:


# 파일 읽기
df5 = pd.read_csv('c:/analysis/과제/아파트 매매 2022.csv', encoding = 'euc-kr', header=15)
df5


# In[29]:


# 거래금액 실수형으로 바꾸기
df5['거래금액(만원)'] = df5['거래금액(만원)'].replace(',', '', regex=True).astype(float)

# 매매 평균 가격 구하기
df5_mean=df5['거래금액(만원)'].mean()

# 시군구별로 그룹화하기
df5_summary_시군구 = df5.groupby(by = '시군구', as_index=False).mean('거래금액(만원)')

# 거래금액 평균으로 구별로 구룹화하기
df5['구'] = df5['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

df5_summary_구 = df5.groupby(by = '구', as_index=False).mean('거래금액(만원)')

# 각 구별 거래건수 구하기
count_per_구_2022 = df5['구'].value_counts()

print(df5_summary_구.columns)


# In[30]:


# 구별로 요약한 자료와 구한 각 구별 거래건수 mergy
df5_summary_구 = pd.merge(df5_summary_구, count_per_구_2022, left_on='구', right_index=True, how='left')


# In[31]:


# 열 이름 바꾸기
df5_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
df5_summary_구.rename(columns={'구_x': '구'}, inplace=True)
df5_summary_구


# In[ ]:





# In[32]:


# 매매 2016,2022년 각 거래건수 총합


# In[33]:


sum_매매거래건수_2016 = df4_summary_구['거래건수'].sum()
sum_매매거래건수_2016


# In[34]:


sum_매매거래건수_2022 = df5_summary_구['거래건수'].sum()
sum_매매거래건수_2022


# In[ ]:





# In[35]:


#3.매매가 변화 추이


# In[36]:


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


# In[37]:


sell_mean = pd.DataFrame({'년도' : [2016,2017,2018,2019,2020,2021,2022],
                     '평균 거래가격' : [ sell2016_mean, sell2017_mean, sell2018_mean, sell2019_mean, sell2020_mean, sell2021_mean, sell2022_mean]})
sell_mean


# In[38]:


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





# In[39]:


# 전월세


# In[40]:


#전월세 파일 읽기

df6 = pd.read_csv('c:/analysis/과제/아파트 전월세 2016.csv', encoding = 'euc-kr', header=15)
df7 = pd.read_csv('c:/analysis/과제/아파트 전월세 2022.csv', encoding = 'euc-kr', header=15)


# In[41]:


df6


# In[42]:


df7


# In[43]:


# 각각 월세, 전세 부분 따로 구별하기

df6_월세 = df6[df6['전월세구분'] == '월세']
df6_전세 = df6[df6['전월세구분'] == '전세']
df7_월세 = df7[df7['전월세구분'] == '월세']
df7_전세 = df7[df7['전월세구분'] == '전세']


# In[44]:


# 2016년 월세 실수형으로 바꾸고 평균 구하기
df6_월세['월세(만원)'] = df6_월세['월세(만원)'].replace(',', '', regex=True).astype(float)

월세2016_mean2=df6_월세['월세(만원)'].mean()
월세2016_mean2

# 2016년 전세 보증금 실수형으로 바꾸고 평균 구하기
df6_전세['보증금(만원)'] = df6_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)

전세2016_mean=df6_전세['보증금(만원)'].mean()
전세2016_mean

# 2022년 월세 실수형으로 바꾸고 평균 구하기
df7_월세['월세(만원)'] = df7_월세['월세(만원)'].replace(',', '', regex=True).astype(float)

월세2022_mean2=df7_월세['월세(만원)'].mean()
월세2022_mean2

# 2022년 전세 보증금 실수형으로 바꾸고 평균 구하기
df7_전세['보증금(만원)'] = df7_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)

전세2022_mean=df7_전세['보증금(만원)'].mean()
전세2022_mean


# In[45]:


# 2016년 월세


# In[46]:


# 2016년 월세 월세 평균으로 구별로 그룹화하기 
df6_월세['구'] = df6_월세['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

월세2016_summary_구 = df6_월세.groupby(by = '구', as_index=False).mean('월세(만원)')

# 각 구별 거래건수 구하기
count_per_구_월세2016 = df6_월세['구'].value_counts()

# 구별로 요약한 자료와 구한 각 구별 거래건수 mergy
월세2016_summary_구 = pd.merge(월세2016_summary_구, count_per_구_월세2016, left_on='구', right_index=True, how='left')

# 열 이름 바꾸기
월세2016_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
월세2016_summary_구.rename(columns={'구_x': '구'}, inplace=True)
월세2016_summary_구


# In[47]:


# 2016년 전세


# In[48]:


# 보증금 평균으로 구별로 그룹화
df6_전세['구'] = df6_전세['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

전세2016_summary_구 = df6_전세.groupby(by = '구', as_index=False).mean('보증금(만원)')

# 거래건수 구하기
count_per_구_전세2016 = df6_전세['구'].value_counts()

# 구별로 요약한 자료와 구한 각 구별 거래건수 mergy
전세2016_summary_구 = pd.merge(전세2016_summary_구, count_per_구_전세2016, left_on='구', right_index=True, how='left')

# 열 이름 바꾸기
전세2016_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
전세2016_summary_구.rename(columns={'구_x': '구'}, inplace=True)


# In[49]:


#2022년 월세


# In[50]:


df7_월세['구'] = df7_월세['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

월세2022_summary_구 = df7_월세.groupby(by = '구', as_index=False).mean('월세(만원)')

count_per_구_월세2022 = df7_월세['구'].value_counts()

월세2022_summary_구 = pd.merge(월세2022_summary_구, count_per_구_월세2022, left_on='구', right_index=True, how='left')

월세2022_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
월세2022_summary_구.rename(columns={'구_x': '구'}, inplace=True)


# In[51]:


#2022년 전세


# In[52]:


df7_전세['구'] = df7_전세['시군구'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

전세2022_summary_구 = df7_전세.groupby(by = '구', as_index=False).mean('보증금(만원)')

count_per_구_전세2022 = df7_전세['구'].value_counts()

전세2022_summary_구 = pd.merge(전세2022_summary_구, count_per_구_전세2022, left_on='구', right_index=True, how='left')

전세2022_summary_구.rename(columns={'구_y': '거래건수'}, inplace=True)
전세2022_summary_구.rename(columns={'구_x': '구'}, inplace=True)
전세2022_summary_구


# In[ ]:





# In[53]:


# 월세, 전세 2016,2022년 각 거래건수 총합


# In[54]:


sum_월세거래건수_2016 = 월세2016_summary_구['거래건수'].sum()
sum_월세거래건수_2016


# In[55]:


sum_월세거래건수_2022 = 월세2022_summary_구['거래건수'].sum()
sum_월세거래건수_2022


# In[56]:


sum_전세거래건수_2016 = 전세2016_summary_구['거래건수'].sum()
sum_전세거래건수_2016


# In[57]:


sum_전세거래건수_2022 = 전세2022_summary_구['거래건수'].sum()
sum_전세거래건수_2022


# In[58]:


# 매매, 월세, 전세 거래건수 변화 추이

t_거래건수변화 = pd.DataFrame({'부동산 유형' : ['매매','월세','전세'],
                         '2016년 총 거래건수' : [ sum_매매거래건수_2016, sum_월세거래건수_2016, sum_전세거래건수_2016], 
                         '2022년 총 거래건수' : [ sum_매매거래건수_2022, sum_월세거래건수_2022, sum_전세거래건수_2022]})

t_거래건수변화


# In[59]:


trace1 = go.Bar(x = t_거래건수변화['부동산 유형'], y = t_거래건수변화['2016년 총 거래건수'], name = '2016')

trace2 = go.Bar(x = t_거래건수변화['부동산 유형'], y = t_거래건수변화['2022년 총 거래건수'], name = '2022')

data5 = [trace1, trace2]

layout = go.Layout(title = '서울특별시 거래건수 변화',
                   xaxis = dict(title = '부동산 유형'),
                   yaxis = dict(title = '총 거래건수'),
                   barmode='group')

fig_거래건수 = go.Figure(data5, layout)
fig_거래건수.show()


# In[ ]:





# In[60]:


#전월세 변화 추이


# In[61]:


#2016
ws2016 = pd.read_csv('c:/analysis/과제/아파트 전월세 2016.csv', encoding = 'euc-kr', header=15)
ws2016_월세 = ws2016[ws2016['전월세구분'] == '월세']
ws2016_전세 = ws2016[ws2016['전월세구분'] == '전세']

ws2016_월세['월세(만원)'] = ws2016_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2016_월세_mean=ws2016_월세['월세(만원)'].mean()

ws2016_전세['보증금(만원)'] = ws2016_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2016_전세_mean=ws2016_전세['보증금(만원)'].mean()


#2017
ws2017 = pd.read_csv('c:/analysis/과제/아파트 전월세 2017.csv', encoding = 'euc-kr', header=15)
ws2017_월세 = ws2017[ws2017['전월세구분'] == '월세']
ws2017_전세 = ws2017[ws2017['전월세구분'] == '전세']

ws2017_월세['월세(만원)'] = ws2017_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2017_월세_mean=ws2017_월세['월세(만원)'].mean()

ws2017_전세['보증금(만원)'] = ws2017_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2017_전세_mean=ws2017_전세['보증금(만원)'].mean()


#2018
ws2018 = pd.read_csv('c:/analysis/과제/아파트 전월세 2018.csv', encoding = 'euc-kr', header=15)
ws2018_월세 = ws2018[ws2018['전월세구분'] == '월세']
ws2018_전세 = ws2018[ws2018['전월세구분'] == '전세']

ws2018_월세['월세(만원)'] = ws2018_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2018_월세_mean=ws2018_월세['월세(만원)'].mean()

ws2018_전세['보증금(만원)'] = ws2018_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2018_전세_mean=ws2018_전세['보증금(만원)'].mean()


#2019
ws2019 = pd.read_csv('c:/analysis/과제/아파트 전월세 2019.csv', encoding = 'euc-kr', header=15)
ws2019_월세 = ws2019[ws2019['전월세구분'] == '월세']
ws2019_전세 = ws2019[ws2019['전월세구분'] == '전세']

ws2019_월세['월세(만원)'] = ws2019_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2019_월세_mean=ws2019_월세['월세(만원)'].mean()

ws2019_전세['보증금(만원)'] = ws2019_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2019_전세_mean=ws2019_전세['보증금(만원)'].mean()


#2020
ws2020 = pd.read_csv('c:/analysis/과제/아파트 전월세 2020.csv', encoding = 'euc-kr', header=15)
ws2020_월세 = ws2020[ws2020['전월세구분'] == '월세']
ws2020_전세 = ws2020[ws2020['전월세구분'] == '전세']

ws2020_월세['월세(만원)'] = ws2020_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2020_월세_mean=ws2020_월세['월세(만원)'].mean()

ws2020_전세['보증금(만원)'] = ws2020_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2020_전세_mean=ws2020_전세['보증금(만원)'].mean()


#2021
ws2021 = pd.read_csv('c:/analysis/과제/아파트 전월세 2021.csv', encoding = 'euc-kr', header=15)
ws2021_월세 = ws2021[ws2021['전월세구분'] == '월세']
ws2021_전세 = ws2021[ws2021['전월세구분'] == '전세']

ws2021_월세['월세(만원)'] = ws2021_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2021_월세_mean=ws2021_월세['월세(만원)'].mean()

ws2021_전세['보증금(만원)'] = ws2021_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2021_전세_mean=ws2021_전세['보증금(만원)'].mean()


#2022
ws2022 = pd.read_csv('c:/analysis/과제/아파트 전월세 2022.csv', encoding = 'euc-kr', header=15)
ws2022_월세 = ws2022[ws2022['전월세구분'] == '월세']
ws2022_전세 = ws2022[ws2022['전월세구분'] == '전세']

ws2022_월세['월세(만원)'] = ws2022_월세['월세(만원)'].replace(',', '', regex=True).astype(float)
ws2022_월세_mean=ws2022_월세['월세(만원)'].mean()

ws2022_전세['보증금(만원)'] = ws2022_전세['보증금(만원)'].replace(',', '', regex=True).astype(float)
ws2022_전세_mean=ws2022_전세['보증금(만원)'].mean()


# In[62]:


# 월세 변화 추이

ws_mean_월세 = pd.DataFrame({'년도' : [2016,2017,2018,2019,2020,2021,2022],
                     '평균 거래가격' : [ ws2016_월세_mean, ws2017_월세_mean, ws2018_월세_mean, ws2019_월세_mean, ws2020_월세_mean, ws2021_월세_mean, ws2022_월세_mean]})
ws_mean_월세


# In[63]:


# 전세 변화 추이

ws_mean_전세 = pd.DataFrame({'년도' : [2016,2017,2018,2019,2020,2021,2022],
                     '평균 거래가격' : [ ws2016_전세_mean, ws2017_전세_mean, ws2018_전세_mean, ws2019_전세_mean, ws2020_전세_mean, ws2021_전세_mean, ws2022_전세_mean]})
ws_mean_전세


# In[64]:


# 월세 변화 추이 그래프

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


# In[65]:


# 전세 변화추이 그래프

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





# In[66]:


########### 지도 만들기 - 매매, 월세, 전세, 청년인구 #############


# In[67]:


# 서울특별시 자치구 shp파일 읽기

import geopandas as gpd

seoul = gpd.read_file('c:/analysis/과제/LARD_ADM_SECT_SGG_11.shp', encoding = 'euc-kr')
seoul.rename(columns={'SGG_NM': '구'}, inplace=True)
seoul


# In[ ]:





# In[68]:


#지도 만들기(매매)


# In[69]:


# 열 이름 바꾸기
df4_summary_구.rename(columns={'거래금액(만원)': '평균거래금액(만원)_2016'}, inplace=True)
df4_summary_구

df5_summary_구.rename(columns={'거래금액(만원)': '평균거래금액(만원)_2022'}, inplace=True)
df5_summary_구


# In[70]:


# 거래금액증감 열 만들기
merged_df = pd.merge(df4_summary_구, df5_summary_구, on='구')
merged_df

average_prices = merged_df.groupby('구')[['평균거래금액(만원)_2016', '평균거래금액(만원)_2022']].mean()
average_prices

average_prices['거래금액증감(만원)'] = average_prices['평균거래금액(만원)_2022'] - average_prices['평균거래금액(만원)_2016']
average_prices


# In[71]:


# 매매 파일과 shp 파일 merge
sell_map = pd.merge(seoul, average_prices, left_on='구', right_index=True, how='left')
sell_map 


# In[72]:


# explore 지도 만들기-거래금액증감을 기준으로

map1=sell_map.explore(cmap = 'YlOrRd',column = '거래금액증감(만원)')
map1


# In[73]:


# 매매 대쉬보드에 올릴 지도 만들기

import plotly.express as px

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





# In[74]:


#지도 만들기 -월세


# In[75]:


월세2016_summary_구.rename(columns={'월세(만원)': '평균월세금액(만원)_2016'}, inplace=True)
월세2016_summary_구

월세2022_summary_구.rename(columns={'월세(만원)': '평균월세금액(만원)_2022'}, inplace=True)
월세2022_summary_구


# In[76]:


# 새로운 열 만들기 - 월세증감

merged_df_월세 = pd.merge(월세2016_summary_구, 월세2022_summary_구, on='구')
merged_df_월세

average_prices_월세 = merged_df_월세.groupby('구')[['평균월세금액(만원)_2016', '평균월세금액(만원)_2022']].mean()
average_prices_월세

average_prices_월세['월세 증감(만원)'] = average_prices_월세['평균월세금액(만원)_2022'] - average_prices_월세['평균월세금액(만원)_2016']
average_prices_월세


# In[77]:


# 만든 월세 파일과 shp파일 merge

월세_map = pd.merge(seoul, average_prices_월세, left_on='구', right_index=True, how='left')
월세_map 


# In[78]:


#explore 지도
map2=월세_map.explore(cmap = 'YlOrRd',column = '월세 증감(만원)')
map2


# In[79]:


# 대시보드에 올릴 월세 지도 - 월세증감 기준으로

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


# In[80]:


#지도 만들기-전세


# In[81]:


전세2016_summary_구.rename(columns={'보증금(만원)': '평균보증금액(만원)_2016'}, inplace=True)
전세2016_summary_구

전세2022_summary_구.rename(columns={'보증금(만원)': '평균보증금액(만원)_2022'}, inplace=True)
전세2022_summary_구

# 전세 보증금 증감 열 새로 만들기
merged_df_전세 = pd.merge(전세2016_summary_구, 전세2022_summary_구, on='구')
merged_df_전세

average_prices_전세 = merged_df_전세.groupby('구')[['평균보증금액(만원)_2016', '평균보증금액(만원)_2022']].mean()
average_prices_전세

average_prices_전세['보증금 증감(만원)'] = average_prices_전세['평균보증금액(만원)_2022'] - average_prices_전세['평균보증금액(만원)_2016']
average_prices_전세


# In[82]:


# 만든 데이터 프레임과 shp파일 merge

전세_map = pd.merge(seoul, average_prices_전세, left_on='구', right_index=True, how='left')
전세_map 


# In[83]:


#explore 지도
map3=전세_map.explore(cmap = 'YlOrRd',column = '보증금 증감(만원)')
map3


# In[84]:


# 대시보드에 올릴 지도 - 전세 보증금 기준

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





# In[85]:


#지도 만들기 - 청년 인구


# In[86]:


# 필요에 따라 문자형, 정수형으로 바꿔주기

pop = pd.read_csv('c:/analysis/과제/서울시 구별 청년인구.csv', encoding = 'utf-8')
pop['2016'].dtype

seoul['구'].dtype

pop['구'] = pop['구'].astype(str)

pop['구'].dtype

seoul['구'] = seoul['구'].astype(str)
pop['구'] = pop['구'].astype(str)

print(pop.index.dtype)


# In[87]:


# 결측치 문제 해결하고 shp파일과 merge

pop.index = pop.index.astype(str)

pop_map = pd.merge(seoul, pop, left_on='구', right_index=True, how='left')
pop_map

print(set(seoul['구'].unique()) - set(pop['구'].unique()))

seoul['구'] = seoul['구'].str.strip().str.lower()
pop['구'] = pop['구'].str.strip().str.lower()

pop_map = pd.merge(seoul, pop, on='구', how='left')
pop_map


# In[88]:


# 청년 인구 감소량 열 만들기

pop_map['청년 인구 증감'] = pop_map['2016'] - pop_map['2022']
pop_map


# In[89]:


# explore 지도
pop_map.explore(cmap = 'PuBu',column = '청년 인구 증감')


# In[90]:


# 청년 지도 만들기 - 인구 감소량으로

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





# In[91]:


#################### 부가자료 ######################


# In[92]:


## 주거 형태 및 점유 형태


# In[93]:


apt = pd.read_csv('c:/analysis/과제/주거실태현황(주택유형,점유형태등)_2020.csv', encoding = 'utf-8', header =1) 
apt


# In[94]:


df_주택유형 = apt.loc[0:5]
df_주택유형


# In[95]:


df_주택유형 = apt.loc[0:5]
df_주택유형


# In[96]:


df_주택점유율 = apt.loc[6:7]
df_주택점유율


# In[97]:


trace = go.Bar(
    x = df_주택유형['주거실태별(2)'],
    y = df_주택유형['서울'],
    ) 

data = [trace]

layout = go.Layout(title = '2020년 기준 서울특별시 주택 유형',
                  xaxis = dict(title = '주택 유형'),
                    yaxis = dict(title = '비율'))


fig_주택유형 = go.Figure(data, layout)
fig_주택유형.show()


# In[98]:


trace = go.Bar(
    x = df_주택점유율['주거실태별(2)'],
    y = df_주택점유율['서울'],
    ) 

data = [trace]

layout = go.Layout(title = '2020년 기준 서울특별시 점유형태',
                  xaxis = dict(title = '점유형태'),
                    yaxis = dict(title = '비율'))


fig_주택점유율 = go.Figure(data, layout)
fig_주택점유율.show()


# In[ ]:





# In[99]:


## 출산율


# In[100]:


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


# In[101]:


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





# In[102]:


text_a="아파트를 선정한 이유는 왼쪽의 표와 같이 2020년 서울특별시 주거 형태에서 아파트가 가장 높은 비율을 차지하고 있었기 때문에 아파트를 기준으로 분석을 실시하였다. 추가적으로 점유 형태를 보면 자가보다 그외가 더 많은 비율을 차지하고 있음을 알 수 있다."


# In[103]:


text_c="위 그래프는 순서대로 서울특별시 평균 매매가, 월세가, 전세 보증금, 서울특별시 전체 거주인구 수 변화 추이(2016~2022년)이다. 왼쪽부터 3개, 부동산 관련 그래프를 보면 전반적으로 2016년부터 2022년까지 증가하는 추세임을 알 수 있다. 그러나 거주인구 수는 2016년부터 2022년까지 꾸준히 감소 중인 것을 볼 수 있다. 즉, 부동산과 거주인구 수가 서로 반비례하는 관계를 가지고 있음을 알 수 있다."


# In[104]:


text_e = "위 그래프는 순서대로 서울특별시 아파트 매매, 월세, 전세 거래 건수의 변화, 그리고 시 전체의 청년 거주 인구수 변화, 자치구별 청년 인구수 변화를 나타낸 것이다(청년의 나이는 만19~39세로 설정). 먼저, 거래 건수의 경우, 매매는 2016년에 비해 2022년에 거래 건수가 확연히 떨어졌으며, 월세와 전세는 2022년에 증가한 것을 알 수 있다. 이는 부동산 가격 상승으로 인한 높은 매매가를 감당하기 힘든 부분에서 매매의 거래 건수는 줄어들고 비교적 월세와 전세의 거래 건수가 증가한 것 같다고 생각한다. 이어서 옆의 청년 인구수를 보면 계속 감소하고 있는 것을 알 수 있다. 성별로 구분했음에도 청년 남자 거주 인구수는 약 14만명이 줄고, 청년 여자 거주 인구수도 약 17만명 줄어들은 것을 알 수 있다. 그리고 자치구별 청년 인구수 또한 일부 자치구를 제외한 대부분의 자치구에서 청년 인구수가 감소하고 있는 것을 알 수 있다. 이러한 청년 인구 수의 감소는 위에서 본 부동산 상승 추이와 거래 건수의 변화 형태에서 간접적으로 이해할 수 있다. "


# In[105]:


text_m="지도는 2016년과 2022년을 바탕으로 구한 자치구별 매매, 월세, 전세 증가율, 그리고 자치구별 청년 인구 감소율이다. 왼쪽은 순서대로 매매, 월세, 전세, 오른쪽은 청년 인구수이다. 부동산 지도의 경우, 진할수록 가격이 많이 상승한 자치구이고, 청년 인구수의 경우, 색이 진할수록 청년의 인구가 많이 감소한 자치구를 나타낸다. 부동산 지도에서 매매, 월세, 전세 모두 비슷하게 강남구, 서초구 등이 진한 부분으로 나타나고 있다. 즉, 이러한 자치구는 부동산 상승폭이 큰 지역이란 뜻이다. 그런데 이때 청년 인구 지도를 보면 진한 부분이 부동산 지도와 비슷한 지역에 분포하고 있다는 것을 파악할 수 있다. 다시 말해, 부동산 상승률이 큰 지역에서 청년 인구 감소율이 컸다는 것을 알 수 있다. "


# In[106]:


text_baby="앞서서 알아본 인구감소는 단지 부동산의 영향만 본 것이다. 그러나 사실 인구수가 감소하는 데에는 여러 요인들이 복합적으로 영향을 미칠 것이다. 당장 왼쪽에 있는 서울특별시 합계출산율 변화 그래프만 봐도 출산율이 줄어들음으로써 인구수가 감소하게 되는 현상이 일어나기 때문이다. 하지만 이러한 출산율 등의 요인에도 불구하고 부동산의 영향을 단지 독립적인 요소로만 볼 수 없다. 왜냐하면 이러한 요인에서도 부동산이 큰 역할을 하고 있기 때문이다. 출산율은 수치만 봤을 때 인구수가 줄어드는 직접적인 요인이지만, 이러한 출산율에 간접적으로 영향을 주는 것이 부동산이기 때문이다. 예를 들어, 출산율이 가장 높은 청년에게 서울 부동산 가격은 큰 부담으로 느껴져 출산하지 않게 되는 경우도 많기 때문이다. 결국 부동산은 인구에 큰 영향을 미친다고 결론 지을 수 있고, 이러한 추세가 연장된다면 부동산 상승과 인구감소 사이의 괴리가 더욱 심해질 수 있으니 이에 대한 방안을 강구할 필요가 있다고 생각한다."


# In[ ]:





# In[107]:


################################# 대시보드 만들기 ####################################


# In[108]:


import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
from plotly.colors import DEFAULT_PLOTLY_COLORS 


# In[ ]:


import pandas as pd
from dash import Dash, dcc, html, Input, Output, State

app = Dash(__name__)
app.title = ('Dashboard | 서울특별시 부동산 상승과 인구 감소 사이의 관계')
server = app.server

# 타이틀
app.layout = html.Div([
    html.H1(dcc.Markdown('<서울특별시 부동산 상승과 청년 인구 감소 간의 관계>'),
            style={'textAlign': 'center',
                   'marginBottom': 10,
                   'marginTop': 10,
                  "font-size": "55px"}),
    
    
    
    
    #서울특별시 주택유형과 점유형태 그래프
    
    html.H2(dcc.Markdown("#서울특별시 주택유형과 점유형태"),
                          style={'float': 'left', 'display': 'inline-block', 'width': '100%', "font-size": "35px"}),
    

    html.Div(className='Graph',
             children=[
                 html.Div(dcc.Graph(id='주택유형', figure=fig_주택유형),
                          style={'float': 'left', 'display': 'inline-block', 'width': '40%'})
             ]),

    html.Div(className='Graph',
             children=[
                 html.Div(dcc.Graph(id='주택점유', figure=fig_주택점유율),
                          
                          style={'float': 'left', 'display': 'inline-block', 'width': '30%'}),
                 
                 
                 # 설명
                 html.Div(dcc.Markdown("아파트를 선정한 이유"),
                          
                          style={'float': 'left', 'display': 'inline-block', 'width': '20%', "font-size": "32px"}),
                 html.Div(dcc.Markdown(text_a),
                          style={'float': 'left', 'display': 'inline-block', 'width': '20%', "font-size": "26px"})
             ]
    ),
    
    
    
    
    # 서울특별시 매매가, 월세가, 전세 보증금, 총 거주인구수 추이
    
    html.H2(dcc.Markdown("#서울특별시 매매가, 월세가, 전세 보증금, 총 거주인구수 추이"),
                          style={'float': 'left', 'display': 'inline-block', 'width': '100%', "font-size": "35px"}),

    
    html.Div(className='Graph',
             children=[
                 html.Div(dcc.Graph(id='매매가격변화 추이', figure=line__매매),
                          style={'float': 'left', 'display': 'inline-block', 'width': '33%'}),
                 
                 
                 html.Div(dcc.Graph(id='월세가격변화 추이', figure=line_월세),
                          style={'float': 'left', 'display': 'inline-block', 'width': '33%'}),
                 
                 
                 html.Div(dcc.Graph(id='전세가격변화 추이', figure=line_전세),
                          style={'float': 'left', 'width': '33%'}),
                 
             ],
             style={'float': 'left', 'width': '70%'}),
    
    
    html.Div([

    html.Div(dcc.Graph(id='서울시 총 인구', figure=fig1),
             style={'float': 'right', 'display': 'inline-block', 'width': '100%'}),
        
    ], style = {'float': 'right', 'width': '30%'}),
    
    
    # 설명
    html.Div(dcc.Markdown(text_c),
                          style={'float': 'left', 'display': 'inline-block', 'width': '100%', "font-size": "26px"}),
     
    
    
    

    # 거래 건수 및 청년 인구수의 변화 그래프
    
    html.H2(dcc.Markdown("#거래건수의 변화와 청년인구수의 변화"),
                          style={'float': 'left', 'display': 'inline-block', 'width': '100%', "font-size": "35px"}),
    
    html.Div([
        html.Div(className='Graph',
                 children=[
                     html.Div(dcc.Graph(id='거래건수', figure=fig_거래건수),
                              style={'float': 'left', 'display': 'inline-block', 'width': '20%'}),
                     
                     html.Div(dcc.Graph(id='청년인구', figure=fig2),
                              style={'float': 'left', 'display': 'inline-block', 'width': '40%'}),
                     
                     html.Div(dcc.Graph(id='구별인구', figure=fig3),
                              style={'float': 'left', 'width': '40%'}),
                 ]),
    ], style={'float': 'right', 'width': '100%'}),
    
    html.Div(dcc.Markdown(text_e),
                          style={'float': 'left', 'display': 'inline-block', 'width': '100%', "font-size": "24px"}),
    
    
    
    
    
    # 자치구별 매매, 월세, 전세 가격 상승과 청년인구 감소 지도로 보기    
    
    html.H2(dcc.Markdown("#자치구별 매매, 월세, 전세 가격 상승과 청년인구 감소 지도로 보기"),
                          style={'float': 'left', 'display': 'inline-block', 'width': '100%', "font-size": "35px"}),
    
    html.Div([
        
    html.Div(className='map',
             children=[
                 html.Div(dcc.Graph(id='매매 상승폭', figure=fig200),
                          style={'float': 'left', 'display': 'inline-block', 'width': '50%'}),
                 
                 html.Div(dcc.Graph(id='월세 상승폭', figure=fig_월세map),
                          style={'float': 'right', 'display': 'inline-block', 'width': '50%'}),

                 html.Div(dcc.Graph(id='전세 상승폭', figure=fig_전세map),
                          style={'float': 'left', 'display': 'inline-block', 'width': '50%'}),
                 
             ]),
    
    ], style = {'float': 'left', 'width': '70%'}),
    
    
    html.Div([
        
    html.Div([
        html.Div(className='map',
                 children=[
                     html.Div(dcc.Graph(id='인구 하락-청년', figure=fig400),
                              style={'float': 'right', 'display': 'inline-block', 'width': '100%'})
                 ]),
        
        
    ], style = {'float': 'right', 'width': '30%'}),
        
     html.Div(dcc.Markdown(text_m),
                                  style={'float': 'left', 'display': 'inline-block', 'width': '100%', "font-size": "24px"}),
        
        
        
        # 부동산의 한계와 영향력, 그리고 그외 인구에 영향을 주는 이외의 요소
        
        html.Div([
        html.H2(dcc.Markdown("#부동산의 한계와 인구에 영향을 미치는 다른 요소, 그리고 부동산의 영향력"),
                          style={'float': 'left', 'display': 'inline-block', 'width': '100%', "font-size": "35px"}),
            
            html.Div(className='Graph',
                     children=[
                         html.Div(dcc.Graph(id='출산율', figure=fig_baby),
                                  style={'float': 'left', 'display': 'inline-block', 'width': '30%'}),
                     ]),
        
        # 설명
        html.Div(dcc.Markdown("인구 감소에 대한 부동산의 영향력"),
                                  style={'float': 'right', 'display': 'inline-block', 'width': '70%', "font-size": "32px"}),
            
        html.Div(dcc.Markdown(text_baby),
                                  style={'float': 'right', 'display': 'inline-block', 'width': '70%', "font-size": "23px"})
            
        ])
    ])
])

# run App
if __name__ == '__main__':
    app.run_server(debug=False, port=8080)


# In[ ]:





# In[ ]:





# In[ ]:




