import matplotlib.pyplot as plt   # imports the pyplot module 

squares = [1, 4, 9, 16, 25] # creates a list called "squares" which holds the data to be plotted. 

fig, ax = plt.subplots()  # variable fig represents the whole figure which is the collection of the plots generated. 
ax.plot(squares, linewidth=3)  #plot method used to plot data given

# set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels.
ax.tick_params(labelsize=14)

plt.show() # open Matplotlib's viewer and displays the plot

