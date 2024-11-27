# Search box for ticker
# drop down for financial statement
# text box for min date
# text box for max date.
# once the user puts a ticker in, it will do a sql query to grab that data
# No other options on the window until it grabs the data and puts it to the screen

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import numpy as np
import pandas as pd

# Create the main window
root = tk.Tk()
root.title('Data Visualization with Tkinter')
root.geometry('600x400')

# Create the widgets for the search box, dropdown, and date inputs
search_var = tk.StringVar()

# Search Entry widget
search_label = ttk.Label(root, text="Enter Ticker Symbol:")
search_label.pack(pady=5)
search_entry = ttk.Entry(root, textvariable=search_var, width=20)
search_entry.pack(pady=5)

# Define a function to plot a Matplotlib graph
def plot_graph():
    # Sample data - this data would pull from your SEC DB
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    # Create a figure and axis
    fig, ax = plt.subplots()
    ax.plot(x, y)
    # This title could be pulled from the data that is chosen to display
    ax.set_title('SEC Data Plot')
    # Displays the figure
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Define a function to update the Matplotlib graph
# def update_graph():
    # Sample data
    # x = [1, 2, 3, 4, 5]
    # y = [3, 5, 7, 9, 11]  # Updated y values
    # Create a figure and axis
    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # ax.set_title('Updated Matplotlib Line Plot')
    # Create a canvas to display the figure
    # canvas = FigureCanvasTkAgg(fig, master=root)
    # canvas.draw()
    # canvas.get_tk_widget().pack()

# Define a function to plot a Seaborn pairplot
# def plot_seaborn_graph():
    # Sample data
    # data = np.random.normal(size=(100, 4))
    # df = pd.DataFrame(data, columns=list('ABCD'))
    # Create a Seaborn pairplot
    # pairplot = sns.pairplot(df)
    # Create a canvas to display the figure
    # canvas = FigureCanvasTkAgg(pairplot.fig, master=root)
    # canvas.draw()
    # canvas.get_tk_widget().pack()


# Create buttons to trigger the graphs
ttk.Button(root, text='Plot Matplotlib Graph', command=plot_graph).pack()

# ttk.Button(root, text='Update Matplotlib Graph', command=update_graph).pack()
# ttk.Button(root, text='Plot Seaborn Graph', command=plot_seaborn_graph).pack()

# Run the application
root.mainloop()