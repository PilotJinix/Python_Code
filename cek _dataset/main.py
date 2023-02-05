import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn import metrics
import missingno as msno

def missing_check(df):
  missing = df.isnull().sum()
  missing_per = round(missing/len(df),4)*100
  unique_val = df.nunique()
  type_data = df.dtypes
  df = pd.DataFrame({'Missing_values':missing,
                    'Percent of Missing (%)':missing_per,
                    'Numbers of Unique':unique_val,
                    'Data type':type_data}).sort_values("Percent of Missing (%)",ascending=False)
  return df

dataset7 = pd.read_excel("dataset/E Commerce Dataset.xlsx", sheet_name=1)
#
# print(missing_check(dataset7))
# print(dataset7.duplicated().sum())
print(dataset7.info())
print(dataset7.describe())
# msno.heatmap(dataset7)
# plt.show()
