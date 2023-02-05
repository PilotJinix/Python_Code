import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import lightgbm as lgb

from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector as selector
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import KBinsDiscretizer, OneHotEncoder


submission = pd.read_csv("format_fraud_detection.csv")
fraud = pd.read_csv("fraud_detection_train.csv")

print(fraud.info())
print(fraud.head())

sns.countplot(x="label", data=fraud)
fig, ax = plt.subplots(figsize=(6, 6))
sns.histplot(fraud, x="umur", hue="label", multiple="stack", ax=ax)
sns.countplot(x="jkpst", hue="label", data=fraud)
# sns.histplot(fraud, x="los", hue="label", multiple="stack", ax=ax)
plt.show()