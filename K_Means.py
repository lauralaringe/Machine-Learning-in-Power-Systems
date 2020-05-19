import numpy as np

class K_Means:
    def __init__(self, k=6, tolerance=0.0001, max_iterations=400):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def fit(self, X):
        self.centroids = {} # Create an empty dictionary containing the centroids


        m = X.shape[0]  # number of data (raws)
        n = X.shape[1]  # number of features in the data

        for i in range(self.k):
            j = np.random.randint(0, m) # randomly pick the first k centroids
            self.centroids[i] = X[j]

        # start of the optimization process
        # main loop
        for i in range(self.max_iterations):
            self.classes = {} # the key will be the centroids and the value will be the datapoint associated

            for i in range(self.k):
                self.classes[i] = []

            for feature in X:
                # calculate the distance between the feature and the centroid
                distances = [np.linalg.norm(feature - self.centroids[centroid]) for centroid in self.centroids]
                # stores the centroid ID that is assigned to the datapoint which is closest to
                classification = distances.index(min(distances)) # take the key of the min distance
                self.classes[classification].append(feature)

            prev_centroids = dict(self.centroids) # save previous centroids in a dictionary

            # Calculate new centroids location
            # as the mean value of all the datapoints assigned to each cluster
            for classification in self.classes:
                self.centroids[classification] = np.average(self.classes[classification], axis=0)

            isOptimal = True


            # check if the algorithm reached the optimal value of the centroids
            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid) / 100.0) > self.tolerance:
                   isOptimal = False
                if isOptimal:
                    break

