import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sci

# Read in data
filepath = 'data.csv'
data = pd.read_csv(filepath, header=0)

# Take column number input from the user and define it as the x variable
column_number = input("Enter the column number you wish to be plotted on the x-axis: ")
x,y = data['Column ' + str(column_number)].sort_values(ascending=True), [1,2,3,4,5,6,7,8,9,10]
y.remove(column_number)

# Select the numbers of rows and columns to make up subplot
#num_rows = 3
#num_cols = 3

# Automatically select the numbers of rows and columns to make up subplot
plot_num = len(y)
if plot_num % 2 == 0:
    num_rows = plot_num / 2
    num_cols = plot_num / num_rows
if plot_num % 3 == 0:
    num_rows = plot_num / 3
    num_cols = plot_num / num_rows
else:
    num_rows = plot_num
    num_cols = 1

# Collect and define the y data
y_vals, y_names = [data["Column "+str(k)] for k in y], [str(k) for k in y]

# Defing a function that removes the first element of a list
def first_drop(C):
    C.pop(0)
    return(C)

# Take challenge number as input from the user
challenge_input = input("Enter the Challenge Number you wish to see results from (1, 2 or 3): ")

# Take a path the user wishes to save the plots to
try: path_input = str(input("Enter the path you wish to save the plots to (if left blank the image will just be displayed): "))
except SyntaxError: path_input = ''
    
# Define a function to plot according to what challenge is selected
def plotter(challenge,column_number,x,y,y_vals,y_names,num_rows,num_cols,path):

    # Challenge 1
    if challenge == 1:

        # Loop though columns and create plots
        for i in range(0,len(y)):
            plt.plot(x,y_vals[i].sort_values(ascending = True),label = 'Column '+y_names[i])

        # Adjust appearance of plots
        plt.title('Plotting Data')
        plt.xlabel('Column '+str(column_number))
        plt.ylabel('All Columns')
        plt.legend(bbox_to_anchor = (1.05,1))
        plt.tight_layout()

    # Challenge 2
    if challenge == 2:

        # Define a curve fitting function
        fit_func = lambda x, A, B: A/(2**x)+B

        # Create grid of empty subplots
        fig, axis = plt.subplots(num_rows,num_cols,sharey=True,sharex=True)

        # Fill the subplots
        y_i = 0
        for i in range(0,num_rows):
            for j in range(0,num_cols):
                # Obtaining statistical results
                sdev,avg = np.std(y_vals[y_i]),np.mean(y_vals[y_i])

                # Creating 2**x fit
                for k in range(3):
                    if k == 0: params, covar = sci.curve_fit(fit_func,x,y_vals[y_i])
                    else: params, covar = sci.curve_fit(fit_func,x,y_vals[y_i], params)
                fit_A,fit_B = params[0],params[1]
                y_fit = map(fit_func, x.tolist(), [fit_A for t in range(x.size)], [fit_B for t in range(x.size)])

                # Creating plots
                axis[i,j].plot(x,y_vals[y_i],'k-',zorder=2)
                axis[i,j].plot(x,y_fit,'k--',alpha=0.5,zorder=3)
                axis[i,j].scatter(x,y_vals[y_i],edgecolor='black',facecolor='white',zorder=4)
                axis[i,j].fill_between(x,avg+sdev,avg-sdev,color='red',alpha=0.2,zorder=1)
                axis[i,j].set_title('Column '+str(column_number)+' vs. '+y_names[y_i],fontsize = 8)
                axis[i,j].tick_params(axis='y',direction='in',right=True)
                axis[i,j].tick_params(axis='x',direction='in',top=True)
                y_i += 1

        # Adjust appearace of plots
        fig.suptitle('Creating Subplots for Data')
        fig.tight_layout()
        plt.subplots_adjust(wspace = 0)

    if path == '':
        plt.show()
    else:
        plt.savefig(path+'\plotted_data_challege_'+str(challenge))

# Output results 
plotter(challenge_input,column_number,x,y,y_vals,y_names,num_rows,num_cols,path_input)

"""
column_number = 1
complete_row_list = [data.iloc[i].tolist() for i in range(0,data.shape[0])]

def first_drop(C):
    C.pop(0)
    return(C)

row_list = map(first_drop, complete_row_list)
col_num_list = range(1,len(row_list)+1)

x = row_list[column_number-1]
row_list.pop(column_number-1)
col_num_list.pop(column_number-1)
for y in range(0,len(row_list)): plt.plot(x,row_list[y],label = 'Column '+str(col_num_list[y]))
plt.legend(loc = 'best')
plt.title('Plotting Results')
plt.show()
"""

#########################################################################################################################

#plot with column 3 = x and column # = y all on one plot
#plot the above plot, but instead of all on one plot do it as a set of 3x3 subplots

    ###
    # BONUS 1 : shares the same y-axis and x-axis with the axes only appearing on bottom plots for x and left plots for y
    ###

    ###
    # BONUS 2 : Put the ticks on the inside of the plot, left and right, top and bottom
    ###

    ###
    # BONUS 3 : draw a red rectangle that is partially see through that is the standard deviation
    ###

    ###
    # BONUS 4 : fit a 1 / 2^x curve to the data
    ###

    ###
    # If a path is given, save the plot to that path, otherwise display the plot
    ###

    ###
    # Use map() in a meaningful way
    ###

    ###
    # Use lambda in a meaningful way
    ###

    ###
    # Use map with lambda in some way (idk how to do this well myself)
    ###

#plot the above with row 1 = x and row # = y as both the above plots
#do this all in under 45 lines

#let me choose which columns I want to plot with a default for plotting all

