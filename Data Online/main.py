#Importing Packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import datetime as dt
from datetime import datetime as dt2
from datetime import timedelta as td
from datetime import time as tm

from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

import plotly.offline as pyoff
import plotly.graph_objs as go

import feature_engine
from feature_engine.outliers import Winsorizer

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
from sklearn.metrics import davies_bouldin_score

import warnings
warnings.filterwarnings("ignore")

df = pd.read_excel('Online Retail.xlsx')
print(df.head())

print(df[df.duplicated()])
df =df[df.Quantity > 0]

#InvoiceDate

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceYearMonth'] = df['InvoiceDate'].map(lambda date: 100*date.year + date.month)
df['Date'] = df['InvoiceDate'].dt.strftime('%Y-%m')

print(df['InvoiceDate'].min())
print(df['InvoiceDate'].max())
print('data 1 tahun')

df =df[df.UnitPrice > 0]

df = df[pd.notnull(df['CustomerID'])]
print(df.info())

df_agg = df.groupby('Date').Quantity.sum()
df_agg = pd.DataFrame(df_agg)
df_agg = df_agg.reindex()

def plot_df(df, x, y, title="", xlabel='Date', ylabel='Quantity', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.plot(x, y, color='tab:Blue', marker='o')
    plt.show()

plot_df(df_agg, x=df_agg.Date, y=df_agg.Quantity,title='Orders in 2011')

df['Revenue'] = df['Quabtity'] * df['UnitPrice']
sns.boxplot(y = df['Revenue'])

df_revenue =df.groupby(['InvoiceYearMonth'])['Revenue'].sum().reset_index()

NOW = dt.date('2011,12,9')
df['Date'] = pd.DataFrameIndex(df.InvoiceDate).date

