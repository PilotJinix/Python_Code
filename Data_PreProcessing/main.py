import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

# pd.set_option('display.max_columns', None)
#
# data = {'Name':['Tom', 'nick', 'krish', 'jack'],
#         'Age':[20, 21, 19, np.nan]}
#
# # df=pd.DataFrame(data)
# # print(df)
#
# df_csv = pd.read_csv("Datasets/DUMMY_DATA.csv",sep=',',header=0, index_col=False)
# # print(df_csv.head(5))
#
# df_excel = pd.read_excel("Datasets/DUMMY_DATA.xlsx", sheet_name=0,header=0,index_col=False)
# # print(df_excel.head(5))
#
# df_json = pd.read_json("Datasets/DUMMY_DATA.json")
# print(df_json.head(5))
#
# df=pd.read_csv("Datasets/marketing_campaign.csv",sep=';')
#
# sns.boxplot(df['Income'])
# plt.show()

test=pd.read_csv(r"Datasets/marketing_campaign.csv",sep=';')
data = test.groupby(['Marital_Status'])[['ID']].count()
data['persen'] = data['ID'] / data['ID'].sum() * 100

cek=['MntWines','MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']

data['expenses'] = data[cek].sum(axis=1)
print(data)