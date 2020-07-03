import gwaffutils
import datetime
import json

new_users = gwaffutils.gethistory()
time = datetime.datetime.today()
with open(f"history/{time}.json", "w") as file:
    json.dump(new_users, file, indent=4)
    file.close()

gwaff = gwaffutils.makegwaff(new_users, time)
with open("gwaff.json", "w") as out:
    json.dump(gwaff, out, indent=4)
