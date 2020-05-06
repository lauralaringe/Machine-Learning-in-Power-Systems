import pandapower as pp

def test_net():
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
    pp.create_sgen(net, b1, p_mw=163, q_mvar=0,name='sgen1')
    pp.create_sgen(net, b2, p_mw=85, q_mvar=0,name='sgen2')

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

    pp.create_load(net, b4, p_mw=110, q_mvar=50, name='load1')
    pp.create_load(net, b6, p_mw=140, q_mvar=60, name='load2')
    pp.create_load(net, b8, p_mw=125, q_mvar=55, name='load3')

    pp.create_gen(net, b0, p_mw=0, name='gen1', slack= True)
    pp.create_sgen(net, b1, p_mw=163, q_mvar=0,name='sgen1')
    pp.create_sgen(net, b2, p_mw=85, q_mvar=0,name='sgen2')

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

    pp.create_load(net, b4, p_mw=70, q_mvar=30, name='load1')
    pp.create_load(net, b6, p_mw=100, q_mvar=50, name='load2')
    pp.create_load(net, b8, p_mw=80, q_mvar=35, name='load3')

    pp.create_gen(net, b0, p_mw=0, name='gen1', slack= True)
    pp.create_sgen(net, b1, p_mw=163, q_mvar=0,name='sgen1')
    pp.create_sgen(net, b2, p_mw=85, q_mvar=0,name='sgen2')

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
    pp.create_sgen(net, b1, p_mw=163, q_mvar=0,name='sgen1')
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
    pp.create_sgen(net, b1, p_mw=163, q_mvar=0,name='sgen1')
    pp.create_sgen(net, b2, p_mw=85, q_mvar=0,name='sgen2')

    return net