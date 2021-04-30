import pandas
from bokeh.plotting import figure, output_file, show

df = pandas.read_csv("adbe.csv", parse_dates=["Date"])

f = figure(width=800, height= 250,x_axis_type="datetime", sizing_mode="stretch_both")

f.line(df["Date"], df["Close"], color = "Orange", alpha=0.5)

output_file("Time_Series.html")
show(f)

