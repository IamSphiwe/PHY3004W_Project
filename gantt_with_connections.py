import plotly.graph_objects as go
import pandas as pd

fig = go.Figure()

df=pd.read_excel('try.xlsx')
f=pd.read_excel('part.xlsx')
g=pd.read_excel('other_part.xlsx')


xar=df['Start']
yar=df['Task']
fig.add_trace(go.Box(
  x = xar,
  y =yar,
  name = "L",
  orientation = "h"
))

fig.update_layout(autosize=False,width=1000,height=1200, title="Gantt Chart showing the Years in which various Physicists Lived",
                  yaxis_title="Physicist",xaxis_title="Year")
fig.update_yaxes(autorange="reversed")

for i in range (0,97):
    fig.add_trace(go.Scatter(y=f.iloc[i], x=g.iloc[i]))
    

#fig.add_trace(go.Scatter(y=['Petrus Peregrinus', 'William Gilbert', 'E. G. von Kleist'], x=['1240','1540','1700']))
#fig.update_layout(title_text="Multi-category axis",)

fig.write_html('gantt_with_connections.html', auto_open=True)
