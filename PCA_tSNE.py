import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def t_SNE(dataset):
    X = np.delete(dataset, -1, axis=1)
    y = dataset[:, -1]

    for i,data in enumerate(y):
        if data =='reference':
            y[i]=0
        if data =='high load':
            y[i]=1
        if data =='low load':
            y[i]=2
        if data =='no gen':
            y[i]=3
        if data =='no line':
            y[i]=4
        if data =='no load':
            y[i]=5

    tsne = TSNE(n_components=2, random_state=0)
    X_2d = tsne.fit_transform(X)
    target_ids = range(6)
    target_names = ['reference', 'high load', 'low load', 'no gen', 'no line', 'no load']
    from matplotlib import pyplot as plt
    plt.figure(figsize=(6, 5))
    colors = 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w', 'orange', 'purple'
    for i, c, label in zip(target_ids, colors, target_names):
        plt.scatter(X_2d[y == i, 0], X_2d[y == i, 1], c=c, label=label)

    plt.title('tSNE', fontsize = 15)
    plt.legend()
    plt.show()

def pca(df):
    features = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    x = df.loc[:, features].values
    # Separating out the target
    y = df.loc[:,["Feature"]].values
    # Standardizing the features
    x = StandardScaler().fit_transform(x)
    # Create a random permutation
    np.random.seed(42)
    rndperm = np.random.permutation(df.shape[0])

    # PCA
    #d tries to provide a minimum number of variables that keeps
    # the maximum amount of variation or information about how the original data is distributed.
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(x)
    principalDf = pd.DataFrame(data = principalComponents
                 , columns = ['Time Steps', 'Voltage'])
    finalDf = pd.concat([principalDf, df[['Feature']]], axis = 1)
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('Time Steps', fontsize = 15)
    ax.set_ylabel('Voltage', fontsize = 15)
    ax.set_title('PCA', fontsize = 15)
    targets = ['reference', 'high load', 'low load', 'no gen', 'no line', 'no load']
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf['Feature'] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'Time Steps']
                   , finalDf.loc[indicesToKeep, 'Voltage']
                   , c = color
                   , s = 50)
    ax.legend(targets)
    ax.grid()
    plt.show()