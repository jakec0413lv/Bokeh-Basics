from bokeh.plotting import figure
from bokeh.io import output_file, show

#Data [Lists must have same length]
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

#Prepare Output File
output_file("Line.html")

#Create figure object
f = figure()

#Create line plot
f.line(x,y)

#Write the plot in the figure object
show(f)
