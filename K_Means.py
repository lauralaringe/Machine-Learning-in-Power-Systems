import os
import numpy as np
import pandas as pd
import math
import random as rd
import matplotlib.pyplot as plt

class K_Means:
    def __init__(self, k=3, tolerance=0.0001, max_iterations=500):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def fit(self, dataset):
        self.centroids = {} # Create an empty dictionary containing the centroids
        X = dataset

        m = X.shape[0]  # number of training data
        n = X.shape[1]  # number of features in the data

        for i in range(self.k):
            j = np.random.randint(0, m) # randomly pick the first k centroids
            #self.centroids[i] = X[i]
            self.centroids[i] = X[j]

        # start of the optimization process
        # main loop
        for i in range(self.max_iterations):
            self.classifications = {} # the key will be the centroids and the value will be the datapoint associated

            for i in range(self.k):
                self.classifications[i] = []

            for feature in X:
                # calculate the distance between the feature and the centroid
                distances = [np.linalg.norm(feature - self.centroids[centroid]) for centroid in self.centroids]
                # stores the centroid ID that is assigned to the datapoint which is closest to
                classification = distances.index(min(distances))
                self.classifications[classification].append(feature)


            prev_centroids = dict(self.centroids) # save previous centroids in a dictionary

            # Calculate new centroids location
            # as the mean value of all the datapoints assigned to each cluster
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            isOptimal = True


            # check if the algorithm reached the optimal value of the centroids
            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                # if the percentage change in the centroid values is lower than the accepted value of tolerance
                if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > self.tolerance:
                    print(np.sum((current_centroid - original_centroid) / original_centroid * 100.0))
                    isOptimal = False
                if isOptimal:
                    break

    def predict(self, dataset):
        distances = [np.linalg.norm(dataset - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification