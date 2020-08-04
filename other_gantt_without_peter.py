import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import plotly.figure_factory as ff

tc='Table_showing_period_lived_without_peter.xlsx'
df=pd.read_excel(tc)

fig=ff.create_gantt(df)
fig.update_layout(autosize=False,width=1000,height=1000, title="Gantt Chart showing the Years in which various Physicists Lived",
                  yaxis_title="Physicist",xaxis_title="Year")
fig.update_yaxes(autorange="reversed")
fig.write_html('tmp.html', auto_open=True)


