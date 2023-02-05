import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import lightgbm as lgb
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


dataa = pd.read_csv('groceries.csv')
dataa = dataa.fillna(value=0)

data = dataa.head()
print(data)

# making each customers shopping items an identical list
trans = []
for i in range(len(data)):
    trans.append([str(data.values[i,j]) for j in range(0, 32)])

# conveting it into an numpy array
trans = np.array(trans)

# checking the shape of the array
print(trans.shape)

te = TransactionEncoder()
data1 = te.fit(trans).transform(trans)
fixdata = pd.DataFrame(data1, columns=te.columns_)
# getting the shape of the data
# print(fixdata.shape)
# print(fixdata.columns)

apriori(fixdata, min_support = 0.01, use_colnames = True)

frequent_itemsets = apriori(fixdata, min_support = 0.05, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

df['antecedents'] = df['antecedents'].astype('string')

result = frequent_itemsets[(frequent_itemsets['length'] == 2) & (frequent_itemsets['support'] >= 0.01)]
print(result)