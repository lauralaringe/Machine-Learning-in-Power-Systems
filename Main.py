import os
import numpy as np
import pandas as pd
import tempfile
import pandapower as pp
from pandapower.control import ConstControl
from pandapower.timeseries import DFData
from pandapower.timeseries import OutputWriter
from pandapower.timeseries.run_time_series import run_timeseries
import matplotlib.pyplot as plt
import TimeSeries as ts
import Network as n


# Time series, Generate training data for different operating states

net = n.test_net()  # standard network
net_hl = n.test_net_hl() # network high load: higher P and Q value for each load + noise
net_ll = n.test_net_ll() # network high load: smaller P and Q value for each load + noise
net_no_gen = n.test_net_no_gen() # network without the generator at bus 3.
net_no_l = n.test_net_no_l() # network without the line between bus 5 and 6.


output_dir = os.path.join(tempfile.gettempdir(), "time_series")
print("Results can be found in your local temp folder: {}".format(output_dir))
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
ts.timeseries(output_dir, net)

output_dir = os.path.join(tempfile.gettempdir(), "time_series_hl")
print("Results can be found in your local temp folder: {}".format(output_dir))
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
ts.timeseries(output_dir, net_hl)

output_dir = os.path.join(tempfile.gettempdir(), "time_series_ll")
print("Results can be found in your local temp folder: {}".format(output_dir))
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
ts.timeseries(output_dir, net_ll)

output_dir = os.path.join(tempfile.gettempdir(), "time_series_no_gen")
print("Results can be found in your local temp folder: {}".format(output_dir))
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
ts.timeseries(output_dir, net_no_gen)

output_dir = os.path.join(tempfile.gettempdir(), "time_series_no_l")
print("Results can be found in your local temp folder: {}".format(output_dir))
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
ts.timeseries(output_dir, net_no_l)



