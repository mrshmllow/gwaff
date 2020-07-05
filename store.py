from scripts import history, gwaff
import datetime
import json

new_users = history.get()
time = datetime.datetime.today()
with open(f"history/{time}.json", "w") as file:
    json.dump(new_users, file, indent=4)
    file.close()


gwaff = gwaff.generate(new_users, time)
with open("gwaff.json", "w") as out:
    json.dump(gwaff, out, indent=4)
