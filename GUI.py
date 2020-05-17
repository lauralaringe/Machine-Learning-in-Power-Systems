import tkinter as tk
from tkinter import messagebox
from Network import *
import pandapower as pd


def callback_network(*args):
    labelTest.configure(text="Choose the node to display the information:")
    labelTest.configure(text ="name: {}" .format(variable.get()))
    net_name = "{}".format(variable.get())
    OptionList = list(pd.pp_elements(net_name))
    opt = tk.OptionMenu(app, variable, *OptionList)
    opt.config(width=200, font=('Helvetica', 12))
    opt.pack(side="top")

def callback(*args):
    #labelTest.configure(text ="element name: {}" .format(variable.get()))
    element = "{}".format(variable.get())
    if net_name == "test_net":
        net = test_net()
    elif net_name == "test_net_hl":
        net = test_net_hl()
    elif net_name == "test_net_ll":
        net = test_net_ll()
    elif net_name == "test_net_no_gen":
        net = test_net_no_gen()
    elif net_name == "test_net_no_l":
        net = test_net_no_l()

    if element == "bus":
        print(net.bus)
    elif element == "ext_grid":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))
    elif element == "gen":
        print(net.gen)
    elif element == "impedance":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))
    elif element == "measurment":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))
    elif element == "switch":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))
    elif element == "storage":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))
    elif element == "ward":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))
    elif element == "xward":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))
    elif element == "load":
        print(net.load)
    elif element == "sgen":
        print(net.sgen)
    elif element == "shunt":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))
    elif element == "trafo":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))
    elif element == "trafo3w":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))
    elif element == "line":
        print(net.line)
    elif element == "dcline":
        answer = messagebox.showinfo(title="Assignment 2, Laura Laringe", message=("Element doesn't exist"
                                                                                   " choose another "))


OptionList = ["test_net", "test_net_hl", "test_net_ll", "test_net_no_gen", "test_net_no_l"]
app = tk.Tk()
app.geometry('700x400')

variable = tk.StringVar(app)
variable.set(OptionList[0])

tk.Label(app, text="Select a network")
opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=200, font=('Helvetica', 12))
opt.pack(side="top")

variable.trace("w", callback_network)

net_name = "{}".format(variable.get())
OptionList = list(pd.pp_elements(net_name))
variable = tk.StringVar(app)
variable.set(OptionList[0])
tk.Label(app, text="Select an element")
opt = tk.OptionMenu(app, variable, *OptionList)

variable.trace("w", callback)

labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

app.mainloop()


plt.show()