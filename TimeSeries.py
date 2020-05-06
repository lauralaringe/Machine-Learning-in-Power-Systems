import numpy as np
import pandas as pd
import pandapower as pp
from pandapower.control import ConstControl
from pandapower.timeseries import DFData
from pandapower.timeseries import OutputWriter
from pandapower.timeseries.run_time_series import run_timeseries


def timeseries(output_dir, net):

    # create (random) data source
    n_timesteps = 70
    profiles, ds = create_data_source(n_timesteps)
    # create controllers (to control P values of the load and the gen)
    net = create_controllers(net, ds)
    # time steps to be calculated. Could also be a list with non-consecutive time steps
    time_steps = range(0, n_timesteps)
    # the output writer with the desired results to be stored to files.
    ow = create_output_writer(net, time_steps, output_dir)
    # the main time series function
    run_timeseries(net, time_steps)



def create_data_source(n_timesteps=70):
    profiles = pd.DataFrame()
    profiles['load1_p'] = np.random.random(n_timesteps) * 20.
    profiles['sgen1_p'] = np.random.random(n_timesteps) * 20.

    ds = DFData(profiles)

    return profiles, ds

def create_controllers(net, ds):
    load1= pp.get_element_index(net, "load", 'load1')
    sgen1 = pp.get_element_index(net, "sgen", 'sgen1')
    ConstControl(net, element='load', variable='p_mw', element_index=[load1],
                 data_source=ds, profile_name=["load1_p"])
    ConstControl(net, element='sgen', variable='p_mw', element_index=[sgen1],
                 data_source=ds, profile_name=["sgen1_p"])
    return net


def create_output_writer(net, time_steps, output_dir):
    ow = OutputWriter(net, time_steps, output_path=output_dir, output_file_type=".xls", log_variables=list())
    # these variables are saved to the harddisk after / during the time series loop
    ow.log_variable('res_load', 'p_mw')
    ow.log_variable('res_bus', 'vm_pu')
    ow.log_variable('res_line', 'loading_percent')
    ow.log_variable('res_line', 'i_ka')
    return ow
