from pandas import read_excel, DataFrame

dataset = read_excel("exams.xlsx")
print(dataset.shape)
x1 = list(dataset.loc[:, "gender"].mode())[0]
l1 = []
for i in dataset.loc[:, "gender"]:
    if (str(i) == "nan"):
        l1.append(x1)
    else:
        l1.append(str(i))

x2 = list(dataset.loc[:, "race/ethnicity"].mode())[0]
l2 = []
for i in dataset.loc[:, "race/ethnicity"]:
    if (str(i) == "nan"):
        l2.append(x2)
    else:
        l2.append(str(i))

x3 = list(dataset.loc[:, "parental level of education"].mode())[0]
l3 = []
for i in dataset.loc[:, "parental level of education"]:
    if (str(i) == "nan"):
        l3.append(x3)
    else:
        l3.append(str(i))

x4 = list(dataset.loc[:, "lunch"].mode())[0]
l4 = []
for i in dataset.loc[:, "lunch"]:
    if (str(i) == "nan"):
        l4.append(x4)
    else:
        l4.append(str(i))

x5 = list(dataset.loc[:, "test preparation course"].mode())[0]
l5 = []
for i in dataset.loc[:, "test preparation course"]:
    if (str(i) == "nan"):
        l5.append(x5)
    elif (str(i) == "none"):
        l5.append("not completed")
    else:
        l5.append(str(i))

x6 = list(dataset.loc[:, "math score"].mode())[0]
l6 = []
for i in dataset.loc[:, "math score"]:
    if (str(i) == "nan"):
        l6.append(x6)
    elif (i < 0):
        l6.append(0)
    elif (i > 100):
        l6.append(100)
    else:
        l6.append(i)

x7 = list(dataset.loc[:, "reading score"].mode())[0]
l7 = []
for i in dataset.loc[:, "reading score"]:
    if (str(i) == "nan"):
        l7.append(x7)
    elif (i < 0):
        l6.append(0)
    elif (i > 100):
        l6.append(100)
    else:
        l7.append(i)

x8 = list(dataset.loc[:, "writing score"].mode())[0]
l8 = []
for i in dataset.loc[:, "writing score"]:
    if (str(i) == "nan"):
        l8.append(x8)
    elif (i < 0):
        l8.append(0)
    elif (i > 100):
        l8.append(100)
    else:
        l8.append(i)
l9 = []
for i in range(0, 1000):
    if (dataset["math score"][i] < 50 and dataset["writing score"][i] < 50 and dataset["reading score"][i] < 50):
        l9.append("fail")
    else:
        l9.append("pass")
# newData = DataFrame({"gender": l1, "race/ethnicity": l2, "parental level of education": l3, "lunch": l4,
#                      "test preparation course": l5, "math score": l6, "reading score": l7, "writing score": l8 , "status" : l9})
# newData.to_excel("Cleaned_Data.xlsx")
