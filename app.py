#!/usr/bin/env python
# coding: utf-8

# In[12]:


import dash  
import dash_core_components as dcc
import dash_html_components as html


# In[15]:


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# step 1. Data Import
data = pd.read_csv("avocado.csv", index_col=0)
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

# step 2. Dash Class
app = dash.Dash(__name__)


# In[ ]:




