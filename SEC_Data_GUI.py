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

# Define a function to plot a Matplotlib graph
def plot_graph():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    # Create a figure and axis
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Matplotlib Line Plot')
    # Create a canvas to display the figure
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Define a function to update the Matplotlib graph
def update_graph():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [3, 5, 7, 9, 11]  # Updated y values
    # Create a figure and axis
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Updated Matplotlib Line Plot')
    # Create a canvas to display the figure
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Define a function to plot a Seaborn pairplot
def plot_seaborn_graph():
    # Sample data
    data = np.random.normal(size=(100, 4))
    df = pd.DataFrame(data, columns=list('ABCD'))
    # Create a Seaborn pairplot
    pairplot = sns.pairplot(df)
    # Create a canvas to display the figure
    canvas = FigureCanvasTkAgg(pairplot.fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create buttons to trigger the graphs
ttk.Button(root, text='Plot Matplotlib Graph', command=plot_graph).pack()
ttk.Button(root, text='Update Matplotlib Graph', command=update_graph).pack()
ttk.Button(root, text='Plot Seaborn Graph', command=plot_seaborn_graph).pack()

# Run the application
root.mainloop()