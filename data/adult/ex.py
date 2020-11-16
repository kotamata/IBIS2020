import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

new_data = pd.read_csv('pre_adult4.csv', index_col=0)
#print(data.head())

import matplotlib.colors as mcolors
colors = list(mcolors.BASE_COLORS.keys())

fig = plt.figure(figsize=(8,8))
ax = Axes3D(fig)

labels = set(new_data['label'])
for idx, label in enumerate(labels):
    df2 = new_data[new_data['label'] == label]
    X = df2["age"]
    Y = df2["education_num"]
    Z = df2["sex"]
    p=ax.scatter(X, Y, Z, c=colors[idx], label=label)

ax.set_xlabel('age')  # X軸ラベル
ax.set_ylabel('education_num')  # Y軸ラベル
ax.set_zlabel('sex')  # Z軸ラベル

plt.legend()
plt.show()

