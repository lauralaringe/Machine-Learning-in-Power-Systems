import pandapower as pp
import numpy as np

# Reference power in the load
p1 = 90
q1 = 30
p1=125
q2=50
p3 = 100
q3 = 35

# Reference power in the s generator
psg1 = 163
psg2 = 85

def test_net():
    net = pp.create_empty_network()
    pp.set_user_pf_options(net, init_vm_pu = "flat", init_va_degree = "dc",
                           calculate_voltage_angles=True)

    b0 = pp.create_bus(net, p_mw=0, q_mw=0, vn_kv=110, name= "bus0")
    b1 = pp.create_bus(net, p_mw=163, q_mw=0, vn_kv=110, name= "bus1")
    b2 = pp.create_bus(net, p_mw=85, q_mw=0, vn_kv=110, name= "bus2")
    b3 = pp.create_bus(net, vn_kv=110, name= "bus3")
    b4 = pp.create_bus(net, p_mw=90, q_mw=30, vn_kv=110, name= "bus4")
    b5 = pp.create_bus(net, vn_kv=110, name= "bus5")
    b6 = pp.create_bus(net, p_mw=100, q_mw=35, vn_kv=110, name= "bus6")
    b7 = pp.create_bus(net, vn_kv=110, name= "bus7")
    b8 = pp.create_bus(net, p_mw=125, q_mw=50, vn_kv=110, name= "bus8")

    pp.create_line(net, b0, b3, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b1, b7, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b3, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b7, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b3, b4, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b7, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b5, b6, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b5, b4, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b2, b5, 10, "149-AL1/24-ST1A 110.0")

    pp.create_load(net, b4, p_mw=90, q_mvar=30, name='load1')
    pp.create_load(net, b6, p_mw=125, q_mvar=50, name='load2')
    pp.create_load(net, b8, p_mw=100, q_mvar=35, name='load3')

    pp.create_gen(net, b0, p_mw=0, name='gen1', slack= True)
    pp.create_sgen(net, b1, p_mw=psg1, q_mvar=0,name='sgen1')
    pp.create_sgen(net, b2, p_mw=psg2, q_mvar=0,name='sgen2')

    return net

def test_net_hl():
    net = pp.create_empty_network()
    pp.set_user_pf_options(net, init_vm_pu = "flat", init_va_degree = "dc",
                           calculate_voltage_angles=True)

    b0 = pp.create_bus(net, p_mw=0, q_mw=0, vn_kv=110)
    b1 = pp.create_bus(net, p_mw=163, q_mw=0, vn_kv=110)
    b2 = pp.create_bus(net, p_mw=85, q_mw=0, vn_kv=110)
    b3 = pp.create_bus(net, vn_kv=110)
    b4 = pp.create_bus(net, p_mw=90, q_mw=30, vn_kv=110)
    b5 = pp.create_bus(net, vn_kv=110)
    b6 = pp.create_bus(net, p_mw=100, q_mw=35, vn_kv=110)
    b7 = pp.create_bus(net, vn_kv=110)
    b8 = pp.create_bus(net, p_mw=125, q_mw=50, vn_kv=110)

    pp.create_line(net, b0, b3, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b1, b7, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b3, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b7, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b3, b4, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b7, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b5, b6, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b5, b4, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b2, b5, 10, "149-AL1/24-ST1A 110.0")

    pp.create_load(net, b4, p_mw=110+np.random.normal(0, 0.1), q_mvar=50+np.random.normal(0, 0.16), name='load1')
    pp.create_load(net, b6, p_mw=140+np.random.normal(0, 0.05), q_mvar=60+np.random.normal(0, 0.1), name='load2')
    pp.create_load(net, b8, p_mw=125+np.random.normal(0, 0.2), q_mvar=55+np.random.normal(0, 0.1), name='load3')

    pp.create_gen(net, b0, p_mw=0, name='gen1', slack= True)
    pp.create_sgen(net, b1, p_mw=psg1, q_mvar=0,name='sgen1')
    pp.create_sgen(net, b2, p_mw=psg2, q_mvar=0,name='sgen2')

    return net

def test_net_ll():
    net = pp.create_empty_network()
    pp.set_user_pf_options(net, init_vm_pu = "flat", init_va_degree = "dc",
                           calculate_voltage_angles=True)

    b0 = pp.create_bus(net, p_mw=0, q_mw=0, vn_kv=110)
    b1 = pp.create_bus(net, p_mw=163, q_mw=0, vn_kv=110)
    b2 = pp.create_bus(net, p_mw=85, q_mw=0, vn_kv=110)
    b3 = pp.create_bus(net, vn_kv=110)
    b4 = pp.create_bus(net, p_mw=90, q_mw=30, vn_kv=110)
    b5 = pp.create_bus(net, vn_kv=110)
    b6 = pp.create_bus(net, p_mw=100, q_mw=35, vn_kv=110)
    b7 = pp.create_bus(net, vn_kv=110)
    b8 = pp.create_bus(net, p_mw=125, q_mw=50, vn_kv=110)

    pp.create_line(net, b0, b3, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b1, b7, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b3, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b7, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b3, b4, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b7, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b5, b6, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b5, b4, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b2, b5, 10, "149-AL1/24-ST1A 110.0")

    pp.create_load(net, b4, p_mw=70+np.random.normal(0, 0.3), q_mvar=30+np.random.normal(0, 0.1), name='load1')
    pp.create_load(net, b6, p_mw=100+np.random.normal(0, 0.1), q_mvar=50+np.random.normal(0, 0.15), name='load2')
    pp.create_load(net, b8, p_mw=80+np.random.normal(0, 0.2), q_mvar=35+np.random.normal(0, 0.1), name='load3')

    pp.create_gen(net, b0, p_mw=0, name='gen1', slack= True)
    pp.create_sgen(net, b1, p_mw=psg1, q_mvar=0,name='sgen1')
    pp.create_sgen(net, b2, p_mw=psg2, q_mvar=0,name='sgen2')

    return net

def test_net_no_gen():
    net = pp.create_empty_network()
    pp.set_user_pf_options(net, init_vm_pu = "flat", init_va_degree = "dc",
                           calculate_voltage_angles=True)

    b0 = pp.create_bus(net, p_mw=0, q_mw=0, vn_kv=110)
    b1 = pp.create_bus(net, p_mw=163, q_mw=0, vn_kv=110)
    b2 = pp.create_bus(net, p_mw=85, q_mw=0, vn_kv=110)
    b3 = pp.create_bus(net, vn_kv=110)
    b4 = pp.create_bus(net, p_mw=90, q_mw=30, vn_kv=110)
    b5 = pp.create_bus(net, vn_kv=110)
    b6 = pp.create_bus(net, p_mw=100, q_mw=35, vn_kv=110)
    b7 = pp.create_bus(net, vn_kv=110)
    b8 = pp.create_bus(net, p_mw=125, q_mw=50, vn_kv=110)

    pp.create_line(net, b0, b3, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b1, b7, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b3, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b7, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b3, b4, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b7, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b5, b6, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b5, b4, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b2, b5, 10, "149-AL1/24-ST1A 110.0")

    pp.create_load(net, b4, p_mw=90, q_mvar=30, name='load1')
    pp.create_load(net, b6, p_mw=125, q_mvar=50, name='load2')
    pp.create_load(net, b8, p_mw=100, q_mvar=35, name='load3')

    pp.create_gen(net, b0, p_mw=0, name='gen1', slack= True)
    pp.create_sgen(net, b1, p_mw=psg1, q_mvar=0,name='sgen1')
    #pp.create_sgen(net, b2, p_mw=85, q_mvar=0,name='sgen2')

    return net

def test_net_no_l():
    net = pp.create_empty_network()
    pp.set_user_pf_options(net, init_vm_pu = "flat", init_va_degree = "dc",
                           calculate_voltage_angles=True)

    b0 = pp.create_bus(net, p_mw=0, q_mw=0, vn_kv=110)
    b1 = pp.create_bus(net, p_mw=163, q_mw=0, vn_kv=110)
    b2 = pp.create_bus(net, p_mw=85, q_mw=0, vn_kv=110)
    b3 = pp.create_bus(net, vn_kv=110)
    b4 = pp.create_bus(net, p_mw=90, q_mw=30, vn_kv=110)
    b5 = pp.create_bus(net, vn_kv=110)
    b6 = pp.create_bus(net, p_mw=100, q_mw=35, vn_kv=110)
    b7 = pp.create_bus(net, vn_kv=110)
    b8 = pp.create_bus(net, p_mw=125, q_mw=50, vn_kv=110)

    pp.create_line(net, b0, b3, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b1, b7, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b3, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b7, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b3, b4, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b7, b8, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b5, b6, 10, "149-AL1/24-ST1A 110.0")
    #pp.create_line(net, b5, b4, 10, "149-AL1/24-ST1A 110.0")
    pp.create_line(net, b2, b5, 10, "149-AL1/24-ST1A 110.0")

    pp.create_load(net, b4, p_mw=90, q_mvar=30, name='load1')
    pp.create_load(net, b6, p_mw=125, q_mvar=50, name='load2')
    pp.create_load(net, b8, p_mw=100, q_mvar=35, name='load3')

    pp.create_gen(net, b0, p_mw=0, name='gen1', slack= True)
    pp.create_sgen(net, b1, p_mw=psg1, q_mvar=0,name='sgen1')
    pp.create_sgen(net, b2, p_mw=psg2, q_mvar=0,name='sgen2')

    return net


