from scripts import plot
import datetime
import json

time = datetime.datetime.today()
with open("gwaff.json", "r") as outfile:
    gwaff = json.load(outfile)

plot.bar(gwaff)
plot.line(gwaff)
