from pandas import read_excel
from sklearn import svm
from sklearn.model_selection import train_test_split
from  sklearn.metrics import  accuracy_score
dataset = read_excel("Cleaned_Data.xlsx")

x = dataset.loc[:,['math score' , "writing score" , 'reading score']]

y = dataset['status']

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size=0.3)

classifier = svm.SVC(kernel="rbf")
classifier.fit(x_train , y_train)

predictions = classifier.predict(x_test)

acc = accuracy_score(y_test , predictions)
print(acc)
