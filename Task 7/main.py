import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pywedge as pw

source = pd.read_excel("dataset-somalia-tax.csv.xlsx", sheet_name=0,header=0,index_col=False)
data = source.groupby(['Province'])[['CompanyID']].count()
# data.plot(
#     kind='bar',
#     title='Perusahaan Tiap Provinsi',
#     ylabel='Jumlah Perusahaan',
#     xlabel='Provinsi',
#     figsize=(10, 6),
#     color= '#009E3C'
# )
# plt.show()

# tax_income = source.sort_values('Tax_Income')[::-1].head()
# colors = sns.color_palette('pastel')[0:5]
# tax = list(tax_income['Tax_Income'].values)
# comp = list(tax_income['CompanyID'].values)
#
# plt.figure(figsize=(15,8))
# sns.barplot(x = tax,y= comp)

# data_presentase = source.groupby(['Kind'])[['CompanyID']].count().reset_index()
# colors = sns.color_palette('pastel')[0:5]
# sum = list(data_presentase['CompanyID'].values)
# label = list(data_presentase['Kind'].values)
# plt.pie(sum, labels = label, colors = colors, autopct='%.0f%%')

custom = source.groupby(['Industry'])[['CompanyID']].count()
custom.plot(
    kind='bar',
    title='Perusahaan Tiap Provinsi',
    ylabel='Jumlah Perusahaan',
    xlabel='Provinsi',
    figsize=(10, 6),
    color= '#009E3C'
)
plt.show()




# source2= pd.read_csv("botak.csv",sep=',',header=0, index_col=False)
# mc = pw.Pywedge_Charts(source2, c=None, y="botak_prob" )
# # For Visualization
# chart = mc.make_charts()

# plt.show()
# print(tax_income[['Tax_Income']])