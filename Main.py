import random
import numpy as np
from sklearn.model_selection import train_test_split
import csv
import tkinter as tk
from DatasetSetup import get_dataset
from DatasetSetup import plot_data
from K_Means import K_Means
from KNN import knn


df_all,dataset = get_dataset() # get the dataset from DatasetSetup

#plot the dataset with voltage magnitude as x and angles as y
# the colors are different for each bus and every marker symbol is a different operating state
plot_data(dataset)

random.shuffle(dataset) # Shuffle data
df_all.to_csv('df.csv') # create a csv with the data shuffled

# Create test and training data
X_train, X_test = train_test_split(dataset, test_size=0.2, train_size=0.8)

# Choose K, tolerance and max_iterations
k = 5
tolerance=0.0001 # only for k means
max_iterations=300 # only for k means

# k-means clustering
# get the optimal amount of clusters
dataset = np.delete(dataset, -1, axis=1) # delete feature column to run k means clustering
classif = K_Means(k,tolerance, max_iterations)
classif.fit(dataset)

# create csv with the classifications of the k mean clustering
with open('k-means.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for keys,values in classif.classes.items():
        for line in values:
            writer.writerow([line, keys])


# KNN
predictions = knn(X_train, X_test, k)

# create csv with the classifications of the KNN
with open('knn.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for x in range(len(X_test)):
        writer.writerow([X_test[x], predictions[x]])


from GUI import *
