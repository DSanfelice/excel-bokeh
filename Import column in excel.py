import pandas as pd
from bokeh.plotting import figure, show

#pull the first column data
sheet_input1 = pd.read_excel('/home/flighttest/Documents/RB5 Flight Test Log.xls', sheet_name=0)
x = sheet_input1['Flight #'].values[1,24].tolist()

sheet_input2 = pd.read_excel('/home/flighttest/Documents/RB5 Flight Test Log.xls', sheet_name=0)
y = sheet_input2["Duration (minutes)"].values[1,24].tolist()

#create a new plot with a title and axis label
plot = figure(title="RB5 Flight Time", x_axis_label='Date', y_axis_label='Time')

#add a line redner with legend and line thickness to the plat
plot.line(x, y, legend_label="Minutes of Flight", line_width=15)

#show the results
show(plot)