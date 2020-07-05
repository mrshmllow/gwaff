from scripts import plot, history
import datetime
import json
import argparse


parser = argparse.ArgumentParser(description='mee6 xp graphing')
parser.add_argument('-p', help='Use this if you want to plot', action='store_true')
parser.add_argument('-s', help='Use this if you want to store', action='store_true')
args = parser.parse_args()

if parser.parse_args().s:
    print("Saving...")
    new_users = history.get()
    time = datetime.datetime.today()

    gwaff = history.generate_gwaff(new_users, time)
    with open("gwaff.json", "w") as out:
        json.dump(gwaff, out, indent=4)

if parser.parse_args().p:
    print("Plotting...")

    time = datetime.datetime.today()
    with open("gwaff.json", "r") as outfile:
        gwaff = json.load(outfile)

    plot.bar(gwaff)
    plot.line(gwaff)