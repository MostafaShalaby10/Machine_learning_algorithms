from pandas import read_excel
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt



dataset = read_excel("Cleaned_Data.xlsx")
x = dataset.loc[:, ['math score', "writing score", 'reading score']]
km = KMeans(n_clusters=3)
predictions = km.fit_predict(x)
dataset['cluster'] = predictions
df1 = dataset[dataset.cluster == 0]
df2 = dataset[dataset.cluster == 1]
df3 = dataset[dataset.cluster == 2]
plt.scatter(df1['reading score'], df1['writing score'], color="red")
plt.scatter(df2['reading score'], df2['writing score'], color="blue")
plt.scatter(df3['reading score'], df3['writing score'], color="green")
plt.show()
list = [] ;
num = range(1 , 10)
for i in num:
    km =KMeans(n_clusters=i)
    km.fit(x)
    list.append(km.inertia_)
plt.plot(num , list)
plt.title("Elbow method")
plt.show()