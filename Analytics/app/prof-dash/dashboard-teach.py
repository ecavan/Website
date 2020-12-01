
import psycopg2
from pprint import pprint
import pandas as pd
import pytz
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from pprint import pprint
import matplotlib.pyplot as plt

from plotly.subplots import make_subplots
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import plotly.figure_factory as ff

from grades_plot import grades_to_plot 
from clust import model, mid, q_avg

from mock_data import get_mock_data

df = get_mock_data()

grades_plot = grades_to_plot(df)

mid = mid(grades_plot)
Q_avg = q_avg(grades_plot)
model = model(mid)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#fig_fan_badge = px.sunburst(df_fan_badge, path=['engagement_class_id', 'fan_badge_id'], values='comments', title = 'Sunburst Graph: Comment type - Fan Badge')
#fig_fan_badge2 = px.sunburst(df_fan_badge, path=['fan_badge_id', 'engagement_class_id'], values='comments', title = 'Sunburst Graph: Fan Badge -  Comment typr')
#fig_gant = px.timeline(df_gant_fig, x_start="start", x_end="end", y="vid")
#fig_gant = ff.create_gantt(df_gant_fig, title = 'Engagement History per Video')
#fig_bubble = px.scatter(df_bubble, x="Response:Comments Ratio", y='Comments:Views Ratio',size="comments", color="video_title", size_max=60, hover_data=['Responses', 'comments', 'video_title', 'video_view_count'], title = 'How responses affect comments & Views')
#fig_bar = px.bar(df_bar_likes, x="video_title", y="Comments:Likes Ratio", color = 'fan_badge', hover_data=['Comments:Likes Ratio', 'comments', 'video_title', 'video_like_count'], title = 'Likes per Comment for a Given fan Badge', labels = {'video_title':''} )
#fig_dist = px.line(df_dist, x="Date", y="video_sum", color='Video', title = '# of Comments after First Response',labels = {'video_sum': 'Total # of Comments'} )
#fig_dist2 = px.line(df_dist_combine, x="dates", y="video_sum", color='video_title')
#fig_bar.update_xaxes(tickangle=60, tickfont=dict(family='Rockwell', size=9))
#fig_bar.update_xaxes(showticklabels=False)
#fig_timeline = px.line(df_user, x="dates", y="# of Comments", color='video_title')
#fig3 = make_subplots(rows=1, cols=2)
#fig3.add_trace(go.Box(y=df2['fan_score']),row=1, col=1)
#fig3.add_trace(go.Box(y=df3['fan_score']),row=1, col=2)
#fig_dist2.add_annotation(x='2020-09-10', y=104,
#          text="First Response",
#           showarrow=True,
#            arrowhead=1)

import plotly.graph_objects as go


fig_grades1 = go.Figure(data=[
    go.Bar(name='Midterm', x=df['Names'], y=grades_plot['Midterm']),
    go.Bar(name='Quiz 1', x=df['Names'], y=grades_plot['Quiz 1']),
    go.Bar(name='Quiz 2', x=df['Names'], y=grades_plot['Quiz 2']),
    go.Bar(name='Quiz 3', x=df['Names'], y=grades_plot['Quiz 3'])
])

fig_grades1.update_layout(barmode='group')


fig_grades2 = px.pie(df, values='Student Rating', names = 'Student Rating', title='Student Ratings')
fig_grades3 = px.scatter(x=df['Names'], y=df['Comments'], title = 'Comments per Student')
fig_grades4 = px.scatter(x=mid["Midterm"], y=Q_avg, color =model.labels_.astype(float) , hover_data = [df['Names']], title = 'Clustering: Midterm Avg v.s Quiz Averages per Student')

app.layout = html.Div(children=[html.H1(children='Professor Dashboards'),html.Div(children='''Analytics to help Professors'''),dcc.Graph(id='example-graph',figure=fig_grades1), dcc.Graph(id='example-graph2',figure=fig_grades2), dcc.Graph(id='example-graph3',figure=fig_grades3), dcc.Graph(id='example-graph4',figure=fig_grades4)])

app.run_server(host='0.0.0.0', port=8050, debug=False)