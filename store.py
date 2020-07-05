from scripts import history, gwaff
import datetime
import json

new_users = history.get()
time = datetime.datetime.today()


gwaff = gwaff.generate(new_users, time)
with open("gwaff.json", "w") as out:
    json.dump(gwaff, out, indent=4)

