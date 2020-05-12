import os
import numpy as np
import pandas as pd
import tempfile
import TimeSeries as ts
import Network as n
from K_Means import K_Means
import matplotlib.pyplot as plt
from matplotlib import style


dataset=pd.read_csv("iris.csv")
X = dataset.values[1:,1:5]
X=(X-X.mean())/X.std() # X normalized

classif = K_Means(3)
classif.fit(X)


colors = 10*["r", "g", "c", "b", "k"]

for centroid in classif.centroids:
    plt.scatter(classif.centroids[centroid][0], classif.centroids[centroid][1],
                marker="o", color="k", s=150, linewidths=5)

for classification in classif.classifications:
    color = colors[classification]
    for feature in classif.classifications[classification]:
        plt.scatter(feature[0], feature[1], marker="x", color=color, s=150, linewidths=5)

plt.show()



