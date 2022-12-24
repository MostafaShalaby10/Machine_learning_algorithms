from pandas import read_excel
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

dataset = read_excel("Cleaned_Data.xlsx")

x = dataset.loc[:, ['writing score']]
y = dataset['reading score']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)

regression = LinearRegression()
regression.fit(x_train, y_train)
predictions = regression.predict(x_test)
print("COF : " , regression.coef_)
print("Intercept : " ,regression.intercept_ )
print("Mean absolute error : ", metrics.mean_absolute_error(y_test, predictions))
print("Mean squared error : ", metrics.mean_squared_error(y_test, predictions))
print("Root mean absolute error : ", np.sqrt(metrics.mean_absolute_error(y_test, predictions)))

dataset.plot(x="writing score", y="reading score", style='o')
plt.plot(x_test, predictions, color="red", linewidth=5)
plt.show()
