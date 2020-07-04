import gwaffutils
import datetime
import json

time = datetime.datetime.today()
with open("gwaff.json", "r") as outfile:
    gwaff = json.load(outfile)

gwaffutils.xpgained(gwaff)
