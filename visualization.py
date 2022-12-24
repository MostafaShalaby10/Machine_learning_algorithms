import colorsys

from pandas import read_excel
from  seaborn import lineplot , scatterplot , barplot , distplot ,displot, boxplot
from  matplotlib import pyplot
newDataSet = read_excel("Cleaned_Data.xlsx")

# lineplot(data=newDataSet["math score"])
# lineplot(data=newDataSet["reading score"])
# lineplot(data=newDataSet["writing score"])


# scatterplot(data=newDataSet["math score"])
# scatterplot(data=newDataSet["reading score"])
# scatterplot(data=newDataSet["writing score"])


# distplot(a=newDataSet["math score"] , bins=3)
# distplot(a=newDataSet["reading score"] , bins=4)
# distplot(a=newDataSet["writing score"] , bins=4 , hist=False)

# displot(data=newDataSet["math score"])
# displot(data=newDataSet["reading score"])
displot(data=newDataSet["writing score"])

# boxplot(data=newDataSet["math score"])
# boxplot(data=newDataSet["reading score"])
# boxplot(data=newDataSet["writing score"])

pyplot.show()