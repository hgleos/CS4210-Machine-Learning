#-------------------------------------------------------------------------
# AUTHOR: Hugo Leos
# FILENAME: clustering.py
# SPECIFICATION: using kmeans to cluster the data
# FOR: CS 4210- Assignment #5
# TIME SPENT: about 2 hours
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn import metrics

df = pd.read_csv('training_data.csv', sep=',', header=None) #reading the data by using Pandas library
X_training = []
S_score = []
#assign your training data to X_training feature matrix
for i in range(len(df)):
     X_training.append(df.iloc[i])

     
#run kmeans testing different k values from 2 until 20 clusters
     #Use:  kmeans = KMeans(n_clusters=k, random_state=0)
     #      kmeans.fit(X_training)
     #--> add your Python code
max_score = 0
for k in range(2, 21):
     kmeans = KMeans(n_clusters=k, random_state=0)
     kmeans.fit(X_training)


     #for each k, calculate the silhouette_coefficient by using: silhouette_score(X_training, kmeans.labels_)
     #find which k maximizes the silhouette_coefficient
     #--> add your Python code here
     S_score.append(silhouette_score(X_training, kmeans.labels_))
     if silhouette_score(X_training, kmeans.labels_) > max_score:
          max_score = silhouette_score(X_training, kmeans.labels_)
          max_k = k

#plot the value of the silhouette_coefficient for each k value of kmeans so that we can see the best k
#--> add your Python code here
plt.plot(range(2, 21), S_score)
plt.show()

#reading the test data (clusters) by using Pandas library
#--> add your Python code here
df = pd.read_csv('testing_data.csv', sep=',', header=None)

#assign your data labels to vector labels (you might need to reshape the row vector to a column vector)
# do this: np.array(df.values).reshape(1,<number of samples>)[0]
#--> add your Python code here
labels = np.array(df.values).reshape(1,len(df))[0]

#Calculate and print the Homogeneity of this kmeans clustering
# print("K-Means Homogeneity Score = " + metrics.homogeneity_score(labels, kmeans.labels_).__str__())
#--> add your Python code here
kmeans = KMeans(n_clusters=max_k, random_state=0)
kmeans.fit(X_training)


print("K-Means Homogeneity Score for k =", max_k, ": " + metrics.homogeneity_score(labels, kmeans.labels_).__str__())