from pandas import read_excel
from sklearn.neighbors import KNeighborsClassifier
from tkinter import *

dataset = read_excel("Cleaned_Data.xlsx")

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(dataset.loc[:, ['math score', 'reading score', 'writing score']], dataset.loc[:, 'status'])

print(knn.predict([
    [20 , 60 , 80],
    [100 , 60 , 80],
    [10 , 20 , 30],
]))

x = Tk()
x.configure(bg="black")
x.title("Predict students' status")
x.minsize(400 , 400)


subject1_label = Label(text ="Subject_1 " , fg="white" , font = "Helvetica 10 bold italic" , bg="black")
subject1_label.place(x=100 , y=50)
# subject1_label.pack()
subject1_value = Entry()
subject1_value.place(x=180 , y=50)
# subject1_value.pack()

subject2_label = Label(text ="Subject_2 " , fg="white" , font = "Helvetica 10 bold italic" , bg="black")
subject2_label.place(x=100 , y=100)
# subject2_label.pack()
subject2_value = Entry()
subject2_value.place(x=180 , y=100)

# subject2_value.pack()

subject3_label = Label(text ="Subject_3 " , fg="white" , font = "Helvetica 10 bold italic" , bg="black")
subject3_label.place(x=100 , y=150)
# subject3_label.pack()
subject3_value = Entry()
subject3_value.place(x=180 , y=150)
# subject3_value.pack()


def predict():

  predictions= knn.predict([[int(subject1_value.get()) , int(subject2_value.get()) ,int(subject3_value.get()) ],])
  result = Label(text="The prediction is : " + predictions , fg="green" , font = "Helvetica 14 bold italic" , bg="black" )
  result.place(y=250 , x=100)
  # result.pack()
btn = Button(text="Predict" , command=predict)
# btn.pack()
btn.place(x=180 , y=200)
x.mainloop()
