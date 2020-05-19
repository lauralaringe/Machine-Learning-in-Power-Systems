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
    net_no_load = n.test_net_no_load()  # network without load 2

    output_dir = os.path.join(tempfile.gettempdir(), "time_series")
    print("Results can be found in your local temp folder: {}".format(output_dir))
    data_folder = Path(output_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df = pd.concat([df1, df2], axis=1, ignore_index=True) # merge voltage magnitude data and voltage angle data
    normalize(df)  # normalize values
    df['Feature'] = 'reference'  # add feature


    output_dir = os.path.join(tempfile.gettempdir(), "time_series_hl")
    data_folder = Path(output_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net_hl)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df_hl = pd.concat([df1, df2], axis=1, ignore_index=True)  # merge voltage magnitude data and voltage angle data
    normalize(df_hl)  # normalize values
    df_hl['Feature'] = 'high load'  # add feature


    output_dir = os.path.join(tempfile.gettempdir(), "time_series_ll")
    data_folder = Path(output_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net_ll)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df_ll = pd.concat([df1, df2], axis=1, ignore_index=True)  # merge voltage magnitude data and voltage angle data
    normalize(df_ll)  # normalize values
    df_ll['Feature'] = 'low load'  # add feature


    output_dir = os.path.join(tempfile.gettempdir(), "time_series_no_gen")
    data_folder = Path(output_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net_no_gen)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df_no_gen = pd.concat([df1, df2], axis=1, ignore_index=True)  # merge voltage magnitude data and voltage angle data
    normalize(df_no_gen)  # normalize values
    df_no_gen['Feature'] = 'no gen'  # add feature


    output_dir = os.path.join(tempfile.gettempdir(), "time_series_no_l")
    data_folder = Path(output_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net_no_l)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df_no_l = pd.concat([df1, df2], axis=1, ignore_index=True)  # merge voltage magnitude data and voltage angle data
    normalize(df_no_l)  # normalize values
    df_no_l['Feature'] = 'no line'  # add feature



    output_dir = os.path.join(tempfile.gettempdir(), "time_series_no_load")
    data_folder = Path(output_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    ts.timeseries(output_dir, net_no_load)
    vm_path = data_folder / "res_bus" / "vm_pu.xls"
    va_path = data_folder / "res_bus" / "va_degree.xls"
    df1 = pd.read_excel(vm_path)
    df2 = pd.read_excel(va_path)
    df_no_load = pd.concat([df1, df2], axis=1, ignore_index=True)  # merge voltage magnitude data and voltage angle data
    normalize(df_no_load)  # normalize values
    df_no_load['Feature'] = 'no load'  # add feature



    # Merge all the operating states data files in one
    df_all = pd.concat([df, df_hl, df_ll, df_no_gen, df_no_l, df_no_load], axis=0, ignore_index=True)
    df_all = df_all.fillna(0)  # fill none values with 0

    df_all = df_all.drop(columns=10)
    df_all = df_all.drop(columns=0)


    dataset = df_all.values

    return df_all,dataset



def plot_data(dataset):
    labels = ['bus1', 'bus2', 'bus3', 'bus4', 'bus5', 'bus6', 'bus7', 'bus8', 'bus9']
    # plot voltage magnitude
    n_of_rows = len(dataset)
    n_of_op_states = 6
    time_steps = n_of_rows / n_of_op_states
    x = time_steps

    reference = dataset[0:int(x-1), :9]
    high_load = dataset[int(x):int(2*x-1), :9]
    low_load = dataset[int(2*x):int(3*x-1), :9]
    no_gen = dataset[int(3*x):int(4*x-1), :9]
    no_line = dataset[int(4*x):int(5*x-1), :9]
    no_load = dataset[int(5*x):int(6*x-1), :9]

    fig, axs = plt.subplots(3, 2)
    axs[0, 0].plot(reference, label=labels)
    axs[0, 0].set_title('Reference')
    axs[0, 1].plot(high_load, label=labels)
    axs[0, 1].set_title('High Load')
    axs[1, 0].plot(low_load, label=labels)
    axs[1, 0].set_title('Low Load')
    axs[1, 1].plot(no_gen, label=labels)
    axs[1, 1].set_title('No generator')
    axs[2, 0].plot(no_line, label=labels)
    axs[2, 0].set_title('No line')
    axs[2, 1].plot(no_load, label=labels)
    axs[2, 1].set_title('No load')

    for ax in axs.flat:
        ax.set(xlabel='Time step', ylabel='Voltage magn.')
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    plt.show()

    # plot voltage angles

    reference = dataset[0:int(x - 1), 9:17]
    high_load = dataset[int(x):int(2 * x - 1),9:17]
    low_load = dataset[int(2 * x):int(3 * x - 1),9:17]
    no_gen = dataset[int(3 * x):int(4 * x - 1), 9:17]
    no_line = dataset[int(4 * x):int(5 * x - 1), 9:17]
    no_load = dataset[int(5 * x):int(6 * x - 1), 9:17]

    fig, axs = plt.subplots(3, 2)
    axs[0, 0].plot(reference, label=labels)
    axs[0, 0].set_title('Reference')
    axs[0, 1].plot(high_load, label=labels)
    axs[0, 1].set_title('High Load')
    axs[1, 0].plot(low_load, label=labels)
    axs[1, 0].set_title('Low Load')
    axs[1, 1].plot(no_gen, label=labels)
    axs[1, 1].set_title('No generator')
    axs[2, 0].plot(no_line, label=labels)
    axs[2, 0].set_title('No line')
    axs[2, 1].plot(no_load, label=labels)
    axs[2, 1].set_title('No load')

    for ax in axs.flat:
        ax.set(xlabel='Time step', ylabel='Voltage angles')
        ax.set_ylim(-8,8)
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    plt.show()

#a,b = get_dataset()
#plot_data(b)

