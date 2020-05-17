import os
import pandas as pd
import matplotlib.pyplot as plt
import tempfile
import TimeSeries as ts
import Network as n
from pathlib import Path



# function to normalize data
def normalize(X):
    return (X-X.mean())/X.std() # X normalized


# Time series, Generate training data for different operating states
def get_dataset():
    net = n.test_net()  # standard network
    net_hl = n.test_net_hl()  # network high load: higher P and Q value for each load + noise
    net_ll = n.test_net_ll()  # network high load: smaller P and Q value for each load + noise
    net_no_gen = n.test_net_no_gen()  # network without the generator at bus 3.
    net_no_l = n.test_net_no_l()  # network without the line between bus 5 and 6.

    output_dir = os.path.join(tempfile.gettempdir(), "time_series")
    # print("Results can be found in your local temp folder: {}".format(output_dir))
    data_folder = Path(output_dir)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df = pd.concat([df1, df2], axis=1)  # merge voltage magnitude data and voltage angle data
    normalize(df)  # normalize values
    df['Feature'] = 'reference'  # add feature
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net)

    output_dir = os.path.join(tempfile.gettempdir(), "time_series_hl")
    # print("Results can be found in your local temp folder: {}".format(output_dir))
    data_folder = Path(output_dir)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df_hl = pd.concat([df1, df2], axis=1)  # merge voltage magnitude data and voltage angle data
    normalize(df_hl)  # normalize values
    df_hl['Feature'] = 'high load'  # add feature
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net_hl)

    output_dir = os.path.join(tempfile.gettempdir(), "time_series_ll")
    # print("Results can be found in your local temp folder: {}".format(output_dir))
    data_folder = Path(output_dir)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df_ll = pd.concat([df1, df2], axis=1)  # merge voltage magnitude data and voltage angle data
    normalize(df_ll)  # normalize values
    df_ll['Feature'] = 'low load'  # add feature
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net_ll)

    output_dir = os.path.join(tempfile.gettempdir(), "time_series_no_gen")
    # print("Results can be found in your local temp folder: {}".format(output_dir))
    data_folder = Path(output_dir)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df_no_gen = pd.concat([df1, df2], axis=1)  # merge voltage magnitude data and voltage angle data
    normalize(df_no_gen)  # normalize values
    df_no_gen['Feature'] = 'no gen'  # add feature
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net_no_gen)

    output_dir = os.path.join(tempfile.gettempdir(), "time_series_no_l")
    # print("Results can be found in your local temp folder: {}".format(output_dir))
    data_folder = Path(output_dir)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df_no_l = pd.concat([df1, df2], axis=1)  # merge voltage magnitude data and voltage angle data
    normalize(df_no_l)  # normalize values
    df_no_l['Feature'] = 'no load'  # add feature
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net_no_l)

    # Merge all the operating states data files in one
    df_all = pd.concat([df, df_hl, df_ll, df_no_gen, df_no_l], axis=0, ignore_index=True)
    df_all = df_all.drop("Unnamed: 0", axis=1)
    df_all = df_all.fillna(0)  # fill none values with 0

    dataset = df_all.values
    return df_all,dataset

# function to plot the dataset with voltage magnitude as x and angles as y
# the colors are different for each bus and every marker symbol is a different operating state
def plot_data(dataset):
    colors = 10 * ["r", "g", "c", "b", "k"]

    for data in dataset:
        if data[-1] == "reference":
            marker = "x"
        elif data[-1] == "high load":
            marker = 'o'
        elif data[-1] == "low load":
            marker = '+'
        elif data[-1] == "no gen":
            marker = '.'
        elif data[-1] == "no load":
            marker = '*'
        plt.scatter(data[0], data[9], marker=marker, color="k", s=150, linewidths=1)
        plt.scatter(data[1], data[10], marker=marker, color='r', s=150, linewidths=1)
        plt.scatter(data[2], data[11], marker=marker, color='g', s=150, linewidths=1)
        plt.scatter(data[3], data[13], marker=marker, color='c', s=150, linewidths=1)
        plt.scatter(data[4], data[14], marker=marker, color='b', s=150, linewidths=1)
        plt.scatter(data[5], data[15], marker=marker, color='w', s=150, linewidths=1)
        plt.scatter(data[6], data[16], marker=marker, color='m', s=150, linewidths=1)
        plt.scatter(data[7], data[17], marker=marker, color='y', s=150, linewidths=1)


    plt.show()