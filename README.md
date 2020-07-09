# Assignment-2-EH2745

## Usage

Main.py contains the main file to run
Network.py contains functions that return panda power networks for different operating states
TimeSeries.py contains the functions to run the timeseries 
K_Means.py contains the k-means clustering algorithm
KNN.py contains the functions for the KNN algorithm
GUI.py containes classes and functions for the running the algorithm
DatasetSetup.py contains the functions to generate the data, execute the time series, merge and normalize the data. It also contains the functions to plot the data.
PCA_tSNE.py contains the code for the visualization of high-dimensional datasets. Since the dataset  in use is 18 dimensions, PCA and tSNE, that are techniques for dimensional reduction have been used to plot the dataset. (The techniques have been used only for visualization purpose)

Running the main, at first the GUI will ask to choose a state and a node to display its information, then it will display the descriptions of how the algorithms are performed. Later, the GUI will ask to choose the timesteps for running the timeseries, if nothing is chosen it will use n=70 as default.
It will ask to plot the data, if yes is chose, it will show the voltage magnitude and angle plots for every state and also 2D visualization with PCA and tSNE techniques. It will ask to choose a k for the KNN algorithm. It is possible to try different k to check the accuracy until close botton is clicked.
N.B. to run the algorithm firther, the windows from the GUI must be closed.

## Results
The results of the algorithm can be seen in two ways:
1. checking the 3 csv files generated: 1 will show the database, with the voltage and the operating state (df.csv), another one will show the k-means with a number on the right that will mean the classification of the object (k-means.py), and the last one will show the classification of the data with the feature for every object (knn.csv)
2. Checking the accuracy printed for the knn algorithm and the number of clusters created for the k-means clustering

The operating states used are 6: Reference, high load, low load, no generator, no line and no load. Their characteristics are descripted in DatasetSetup. The plot of the data will show 2 page with 6 graphs. Each graph represent the voltage magnitide/angle of each bus for the n timesteps.

The results show that the algoritgms work correctly. The k-means with k=6 finds 6 clusters. From the csv file created it can be checked, confronting it with df.csv file that the data classified. Making some checks, the clustering seems to be correct.
The KNN algorithm works very good with more data and low k. It can be checked chaging these parameters in the execution and also checking the knn.csv file.
