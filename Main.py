import random
from sklearn.model_selection import train_test_split
import csv
from DatasetSetup import get_dataset
from DatasetSetup import plot_data
from K_Means import K_Means
from KNN import knn
from GUI import *
from PCA_tSNE import t_SNE, pca


df_all,dataset = get_dataset() # get the dataset from DatasetSetup

#plot the dataset with voltage magnitude as x and angles as y
# the colors are different for each bus and every marker symbol is a different operating state
# Execute PCA and tSNE and plots
response = choose_plot("Do you want to plot the data of the dataset?").response
if response == "1":
    plot_data(dataset)
    t_SNE(dataset)
    pca(df_all)
df_all.to_csv('df.csv') # create a csv with the data not shuffled
random.shuffle(dataset) # Shuffle data


# Create test and training data
X_train, X_test = train_test_split(dataset, test_size=0.2, train_size=0.8)


def create_kmeans_csv(classif):
# create csv with the classifications of the k mean clustering
    with open('k-means.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for keys,values in classif:
            for line in values:
                writer.writerow([line, keys])


def create_knn_csv(X_test):
# create csv with the classifications of the KNN
    with open('knn.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for x in range(len(X_test)):
            writer.writerow([X_test[x], predictions[x]])


#Set k, tolerance and max interations
k = 6
tolerance=0.0001 # only for k means
max_iterations=300 # only for k means
# k-means clustering
# get the optimal amount of clusters
dataset = np.delete(dataset, -1, axis=1) # delete feature column to run k means clustering
#dataset = dataset[:,:-2]

km = K_Means(k,tolerance, max_iterations)
km.fit(dataset)
create_kmeans_csv(km.classes.items())
print(len(km.classes.items()), "clusters created from the k-means algorithm. \n"
                               "Check k-means.csv for more information")


# KNN
flag=False
while not flag:
    k = input_k("Enter k to run the KNN algorithm!").response

    if k is 0 or k is "":
        flag = True
        print("Didn't execute algorithm")
    else:
        k = int(k)
        print("returned value is:", k)
        predictions = knn(X_train, X_test, k)
        create_knn_csv(X_test)

