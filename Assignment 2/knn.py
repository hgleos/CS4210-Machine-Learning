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
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

print(db)
#loop your data to allow each instance to be your test set
testIndex = 0
while testIndex < 10:
    testInstance = []
    for i, instance in enumerate(db):

        #add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
        #For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages

        #transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
        #For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages

        #--> add your Python code here
        # X =
        # Y =
        #testSample =
        resultConversion = {'-' : 0, '+' : 1}

        if testIndex == i:
            testInstance = instance
        else:
            X = [[float(instance[0]), float(instance[1])]]
            Y = [resultConversion[instance[2]]]
            print(X)
            print(Y)

            #fitting the knn to the data
            clf = KNeighborsClassifier(n_neighbors=1, p=2)
            clf = clf.fit(X, Y)

            #use your test sample in this iteration to make the class prediction. For instance:
            #class_predicted = clf.predict([[1, 2]])[0]
            #--> add your Python code here
        if i == 9:
            prediction = clf.predict([[float(testInstance[0]), float(testInstance[1])]])[0]
            print("Prediction is: ", prediction)

            #compare the prediction with the true label of the test instance to start calculating the error rate.
            #--> add your Python code here
    
    testIndex += 1
    print("\n\nNext iteration\n")

#print the error rate
#--> add your Python code here






