import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns
import pywedge as pw

df_csv = pd.read_csv("sample_submission.csv",sep=',',header=0, index_col=False)
data = pd.DataFrame(df_csv)
# print(data['SalePrice'].describe())

data['SalePrice'].plot(kind='hist')


n_bins = 20
legend = ['distribution']

fig, axs = plt.subplots(1, 1,
                        figsize=(10, 7),
                        tight_layout=True)

for s in ['top', 'bottom', 'left', 'right']:
    axs.spines[s].set_visible(False)

axs.xaxis.set_ticks_position('none')
axs.yaxis.set_ticks_position('none')

axs.xaxis.set_tick_params(pad=5)
axs.yaxis.set_tick_params(pad=10)

axs.grid(color='grey',
         linestyle='-.', linewidth=0.5,
         alpha=0.6)

fig.text(0.9, 0.15, 'Data Persebaran Berdasar SalePrice',
         fontsize=12,
         color='red',
         ha='right',
         va='bottom',
         alpha=0.7)

N, bins, patches = axs.hist(data['SalePrice'], bins=n_bins)

fracs = ((N ** (1 / 5)) / N.max())
norm = plt.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

plt.xlabel("Persebaran Data")
plt.ylabel("Frekuensi Data")
plt.legend(legend)
plt.title('SalePrice Perumahan')

# plt.show()

sample = data['SalePrice'].sample(frac=0.95)

print(sample.reindex)