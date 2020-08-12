from graphviz import Digraph
import pandas as pd

df=pd.read_excel('Connections_history_em.xlsx')
dot = Digraph()



for index, row in df.iterrows():
 dot.edge(row["Influencer"], row["Influencee"], label='')



dot.render('Digraph_rough_version.pdf', view=True)












