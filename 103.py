import pandas as pd
import plotly.express as px
df=pd.read_csv('line_chart.csv')
figg=px.line(df,x='Year',y='Per capita income',color='Country',title='PER CAPITA INCOME')
figg.show()
fig=px.bar(df,x='Year',y='Per capita income',title='PER CAPITA INCOME')
fig.show()
fig1=px.scatter(df,x='Year',y='Per capita income',color='Country',size_max=60,title='PER CAPITA INCOME')
fig1.show()