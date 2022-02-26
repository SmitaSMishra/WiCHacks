from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sn
import pylab as pl

data = pd.read_csv('reviews_NewYork.csv')
df = pd.DataFrame(data)
print(data.head)
corrMatrix = df.corr()
print(corrMatrix)
plt.figure(figsize=(8,8))
sn.heatmap(corrMatrix, annot=True)
plt.title("Heatmap for India Combined Data")
plt.show()
