import utils
import datetime
import json


def plot():
    time = datetime.datetime.today()
    with open('gwaff.json', 'r') as outfile:
        gwaff = json.load(outfile)

    utils.xpgained(gwaff)


def store():
    new_users = utils.gethistory()
    time = datetime.datetime.today()
    with open(f"history/{time}.json", "w") as file:
        json.dump(new_users, file, indent=4)
        file.close()
    gwaff = utils.makegwaff(new_users, time)
    with open("gwaff.json", "w") as out:
        json.dump(gwaff, out, indent=4)


plot()
