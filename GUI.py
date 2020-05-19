import tkinter as tk
from tkinter import messagebox
from Network import *
import pandapower as pd
from tkinter import *

def callback_network(*args):
    labelTest.configure(text="Choose the node to display the information:")
    labelTest.configure(text ="name: {}" .format(variable.get()))
    net_name = "{}".format(variable.get())
    OptionList = list(pd.pp_elements(net_name))
    opt = tk.OptionMenu(app, variable, *OptionList)
    opt.config(width=200, font=('Helvetica', 12))
    opt.pack(side="top")

def callback(*args):
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
    elif net_name == "test_net_no_load":
        net = test_net_no_load()

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


OptionList = ["test_net", "test_net_hl", "test_net_ll", "test_net_no_gen", "test_net_no_l", "test_net_no_load"]
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

class choose_plot():
    def __init__ (self, prompt):
        self.prompt = prompt
        self.response = ""

        def ok():
            self.response = "1"
            master.destroy()

        def close():
            master.destroy()

        master = Tk()
        lbl = Label(master, text=self.prompt)
        lbl.pack()
        butt = Button(master, text = "Yes", width = 10, command = ok)
        butt.pack()
        butt2 = Button(master, text="No", width=10, command=close)
        butt2.pack()

        mainloop()


class input_k():
    def __init__ (self, prompt):
        self.prompt = prompt
        self.response = ""

        def submit():
            self.response = entry.get()
            master.destroy()

        def close():
            self.response = 0
            master.destroy()

        master = Tk()
        lbl = Label(master, text=self.prompt)
        lbl.pack()
        entry = Entry(master)
        entry.pack()

        entry.focus_set()

        butt = Button(master, text = "Submit", width = 10, command = submit)
        butt2 = Button(master, text = "Close", width = 10, command = close)
        butt.pack()
        butt2.pack()

        mainloop()



class k_means_info():
    master = tk.Tk()
    intro = "-What is the k-means clustering doing? \n \n Step 0: Prepare the data, shuffle it and normalize it\n \n" \
            "Step 1: Randomly pick the first k centroids \n \n " \
            "Step 2: Calculate the distance of each value from the centroids \n \n Step3: " \
            "Store the centroid ID that is assigned to the datapoint which is closest to \n \n" \
            "Step 4: Save previous centroids in a dictionary" \
            "\n \n Step 5: Calculate new centroids location as the mean value of all the datapoints assigned " \
            "to each cluster \n \n Step 6: Check if the algorithm reached the optimal value of the centroids \n" \
            "\n Step 7: Go to step 3 "
    msg = tk.Message(master, text=intro, width=800, justify='left')
    msg.config(bg='white', font=('times', 13))
    msg.pack()
    tk.mainloop()

class knn_info():
    master = tk.Tk()
    intro = "-What is the KNN algorithm doing? \n \n Step 0: Prepare the data, shuffle it and normalize it. " \
            "It will be a learning set and a test set." \
            "The test set is 20% of the dataset and the learning set is 80%\n \n " \
            "Step 1: Given a i line of the test set calculate the distance between the test line and the learning data" \
            "\n \n Step 2: Calculate the k closest neighbors and append in the list of neighbors in ascending order " \
            "\n \n Step 3: Rank how many points belong to the same feature and take the first one" \
            "\n \n Step 4: Go to step 1 with i+1 "


    msg = tk.Message(master, text=intro,  width=800, justify='left')
    #msg = tk.Message(master, text=intro)
    msg.config(bg='white', font=('times', 13))
    msg.pack()
    tk.mainloop()

