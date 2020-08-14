from graphviz import Digraph
import pandas as pd

df=pd.read_excel('Connections_history_em.xlsx')
dot = Digraph()


colors=df['Colors']
for index, row in df.iterrows():
 dot.edge(row["Influencer"], row["Influencee"],label='',color=row["Colors"])

#dot.attr(color='green')

dot.render('Digraph_rough_version.pdf', view=True)












