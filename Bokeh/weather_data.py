import pandas
from bokeh.plotting import figure, output_file, show
 
df = pandas.read_excel("verlegenhuken.xlsx")

x = df["Temperature"] / 10
y = df["Pressure"] / 10


output_file("Weather_Data.html")

f = figure()

f.title.text="Cool Data"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"

f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Temperature (°C)"
f.yaxis.axis_label="Pressure (hPa)"    

f.circle(x,y, size = 0.5)

show(f)