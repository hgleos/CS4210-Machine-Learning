#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from numpy import append
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)


# variable to alternate the test instance, starts at the first instance
testIndex = 0

print(db)
# loop your data to allow each instance to be your test set
while testIndex < 10:
    X = []
    Y = []

    for i, instance in enumerate(db):

        #add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
        #For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning message

        #transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
        #For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages

        #--> add your Python code here
        if (testIndex == i):
            testInstance = instance
        else:
            X.append([instance[0], instance[1]])
            Y.append(instance[2])

        print(X)

        #fitting the knn to the data
        clf = KNeighborsClassifier(n_neighbors=1, p=2)
        clf = clf.fit(X, Y)

        #use your test sample in this iteration to make the class prediction. For instance:
        #class_predicted = clf.predict([[1, 2]])[0]
        #--> add your Python code here
        class_prediction = clf.predict([testInstance[0], testInstance[1]])

        #compare the prediction with the true label of the test instance to start calculating the error rate.
        #--> add your Python code here
    print(testInstance)
    print(X)
    print(Y)
    testIndex += 1

#print the error rate
#--> add your Python code here






