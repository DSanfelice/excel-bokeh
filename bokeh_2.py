import pandas as pd
from bokeh.plotting import figure, show

#import excel doc
#col1 = pd.read(python excel.ods)
#col1.head()

#col1[col1["Days"] =='']




#add data
x = [1, 2, 3, 4, 5, 6, 7]
y = [4, 9, 7, 2, 3, 1, 8]

#create a new plot with a title and axis label
p = figure(title="Dans plot", x_axis_label='x', y_axis_label='y')

#add a line redner with legend and line thickness to the plat
p.line(x, y, legend_label="Temp", line_width=15)

#show the results
show(p)