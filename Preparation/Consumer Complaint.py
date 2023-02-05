#

# !pip install --upgrade pip
# !pip install pandas-profiling
# !pip install pandas-profiling[notebook]
import inline as inline
import matplotlib
import pandas as pd
import pandas_profiling
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from datetime import datetime

df=pd.read_csv('Consumer_Complaints.csv')
df.columns = df.columns.str.title()
df['Date'] =pd.to_datetime(df['Date Received'])
e_df=pd.DataFrame().from_records([{"empty_prec":np.round(len(df[df[col].isna()])/len(df), 4)*100, "col":col} for col in df.columns])
print(e_df)
print("Dropping Columns with high empty ratio, >60%")
print(e_df[e_df["empty_prec"]>60])
df=df.drop(e_df[e_df["empty_prec"]>60].col.values, axis=1)
df['Sub-Product']=df['Sub-Product'].fillna("Unknown")
df.dropna(subset=['State', 'Zip Code'], inplace=True)
mode_value = df['Consumer Disputed?'].mode().values[0]
df['Consumer Disputed?'].fillna(mode_value, inplace = True)
df['Consumer Disputed?'].isnull().fillna(mode_value, inplace = True)
df['Year'] =df['Date'].dt.year
df['Month'] =df['Date'].dt.month
df['Week_Days'] = df['Date'].dt.day_name()
issue_groups={}
product_groups={}

for issue, group in df.groupby('Issue'):
    mode=group['Sub-Issue'].mode()
    issue_groups[issue]=mode.values[0] if len(mode) else 'NA'
df['Sub-Issue'].fillna('Unknown', inplace=True)
df['Sub-Issue'] = df.apply(lambda x: issue_groups[x['Issue']] if x['Sub-Issue']=='Unknown' else x['Sub-Issue'], axis=1)


for product, group in df.groupby('Product'):
    mode=group['Sub-Product'].mode()
    product_groups[product]=mode.values[0] if len(mode) else 'NA'
df['Sub-Product'].fillna('Unknown', inplace=True)
df['Sub-Product'] = df.apply(lambda x: product_groups[x['Product']] if x['Sub-Product']=='Unknown' else x['Sub-Product'], axis=1)

u_df=pd.DataFrame().from_records([{"unique_prec":np.round(len(df[col].unique())/len(df), 4)*100, "col":col} for col in df.columns])
print("Dropping Columns with high Uniqueness ratio, >50%")
print(u_df[u_df["unique_prec"]>50])
df.drop(u_df[u_df["unique_prec"]>50].col.values, axis=1, inplace=True)

c_df=pd.DataFrame(df['Company'].value_counts()).reset_index().reset_index()
n=1000
print("Dropping Company Values with less than %d complaints, keeping %f%% values, dropping %f%% values"% (n, c_df[c_df['Company']>=n]['Company'].sum()/len(df), c_df[c_df['Company']<n]['Company'].sum()/len(df)))
df=df[df['Company'].isin(c_df[c_df['Company']>=n]['index'].values)]
print("Left with %d Companies"%len(df.Company.unique()))

print("Cleaned Data set, Empty Ratios: \n", pd.DataFrame().from_records([{"empty_prec":np.round(len(df[df[col].isna()])/len(df), 4)*100, "col":col} for col in df.columns]))
print("Cleaned Data set, Empty Ratios: \n", pd.DataFrame().from_records([{"unique_prec":np.round(len(df[col].unique())/len(df), 4)*100, "col":col} for col in df.columns]))
df.head()







# Nomer 2

h, w = 4, 3
_, ax=plt.subplots(h,w, figsize=(w*10,h*7))
top_n=10
df['Product'].value_counts().sort_values(ascending=False)[:top_n].to_frame('counts').sort_values('counts', ascending=True).plot.barh(title='Top Complaints in Products', ax=ax[0][0])
df['Sub-Product'].value_counts().sort_values(ascending=False)[:top_n].to_frame('counts').sort_values('counts', ascending=True).plot.barh(title='Top Complaints in Sub Products', ax=ax[0][1])
df['Company'].value_counts().sort_values(ascending=False)[:top_n].to_frame('counts').sort_values('counts', ascending=True).plot.barh(title='Top 20 Companies with Highest number of Compaints', ax=ax[0][2])
df['Timely Response?'].value_counts().plot.pie(ax=ax[1][0])
df['Company Response To Consumer'].fillna('NA').value_counts().plot.pie(ax=ax[1][1])
df['Issue'].value_counts().sort_values(ascending=False)[:top_n].to_frame('counts').sort_values('counts', ascending=True).plot.barh(title='Top 20 Issues with Highest number of Compaints', ax=ax[1][2])
df['Sub-Issue'].value_counts().sort_values(ascending=False)[:top_n].to_frame('counts').sort_values('counts', ascending=True).plot.barh(title='Top 20 Sub-Issues with Highest number of Compaints', ax=ax[2][0])
df['Submitted Via'].value_counts().plot.pie(title="Platform of Complaint", legend=False, ax=ax[2][1])
df['Consumer Disputed?'].value_counts().plot.pie(title="Is Consumer Disputed", legend=False, ax=ax[2][2])
df.groupby(['Month']).size().plot.bar(title="Complaints by Month", legend=False, ax=ax[3][0])
df.groupby(['Year']).size().plot(title="Complaints by Year", legend=False, ax=ax[3][1])
top_banks=df['Company'].value_counts().sort_values(ascending=False)[:top_n].index
df[df['Company'].isin(top_banks)].groupby(['Year', 'Company']).size().unstack().plot(ax=ax[3][2], marker='^', title='Complaints against companies over years')

plt.tight_layout()