#-------------------------------------------------------------------------
# AUTHOR: Loc Nguyen
# FILENAME: decision_tree.py
# SPECIFICATION: Read input from CSV file and output ID3 decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv,copy
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

newdb = copy.deepcopy(db)


#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =
for i in range(len(newdb)):
   for j in range(len(newdb[i])-1):
      if j == 0:
        match newdb[i][j]:
          case "Young":
            newdb[i][j] = 1
          case "Prepresbyopic":
            newdb[i][j] = 2
          case "Presbyopic":
            newdb[i][j] = 3
      elif j == 1:
        match newdb[i][j]:
          case "Myope":
            newdb[i][j] = 1
          case "Hypermetrope":
            newdb[i][j] = 2
      if j == 2:
        match newdb[i][j]:
          case "Yes":
            newdb[i][j] = 1
          case "No":
            newdb[i][j] = 2
      if j == 3:
        match newdb[i][j]:
          case "Reduced":
            newdb[i][j] = 1
          case "Normal":
            newdb[i][j] = 2

X = newdb
for i in range(len(X)):
  del X[i][4]
print(X)
#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =
for i in range(len(db)):
  Y.append(db[i][4])
  if Y[i] == "Yes":
    Y[i] = 1
  elif Y[i] == "No":
    Y[i] = 2

print(Y)
#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()