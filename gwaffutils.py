import requests
import json
import matplotlib.pyplot as plt
import matplotlib as mpl
from labellines import labelLines
from yaml import safe_load





def gethistory():
    with open("config.yml", "r") as file:
        config = safe_load(file)
    page = 0
    users = {}
    q = 0
    for i in range(int(config["data_range"] / 100)):
        r = requests.get(
            f"https://mee6.xyz/api/plugins/levels/leaderboard/{config['server_id']}?page={str(page)}"
        ).json()
        if "status_code" in r.keys():
            if r["status_code"] == 404:
                exit("guild not found")
        if not r["players"] == []:
            for user in r["players"]:
                if q < config["data_range"] or q == config["data_range"]:
                    users[str(q)] = user
                q += 1
        else:
            break
        page += 1
    return users


def makegwaff(new_users, time):
    with open("gwaff.json") as json_file:
        gwaff = json.load(json_file)
        json_file.close()

    for user in new_users:
        if new_users[user]["id"] not in gwaff:
            gwaff[new_users[user]["id"]] = {
                "name": f"{new_users[user]['username']}#{new_users[user]['discriminator']}",
                "message_count": {str(time): new_users[user]["message_count"]},
                "total_xp": {str(time): new_users[user]["xp"],},
                "detailed_xp": {str(time): new_users[user]["detailed_xp"]},
                "level": {str(time): new_users[user]["level"]},
            }
        else:
            gwaff[new_users[user]["id"]][
                "name"
            ] = f"{new_users[user]['username']}#{new_users[user]['discriminator']}"
            gwaff[new_users[user]["id"]]["message_count"][str(time)] = new_users[user][
                "message_count"
            ]
            gwaff[new_users[user]["id"]]["total_xp"][str(time)] = new_users[user]["xp"]
            gwaff[new_users[user]["id"]]["detailed_xp"][str(time)] = new_users[user][
                "detailed_xp"
            ]
            gwaff[new_users[user]["id"]]["level"][str(time)] = new_users[user]["level"]

    return gwaff


def xpgained(gwaff):
    with open("config.yml", "r") as file:
        config = safe_load(file)

    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(
        color=[
            "blue",
            "green",
            "red",
            "cyan",
            "magenta",
            "yellow",
            "black",
            "purple",
            "pink",
            "brown",
            "orange",
            "teal",
            "coral",
            "lightblue",
            "lime",
            "lavender",
            "turquoise",
            "darkgreen",
            "tan",
            "salmon",
            "gold",
        ]
    )
    if config["darkmode"]:
        plt.style.use("dark_background")
    plt.figure(figsize=(14, 7))
    g = 0
    q = 0
    for user in gwaff:
        if g < config["plot_range"]:
            if q < 19:
                y = [0]
                x = []
                total_xp = gwaff[user]["total_xp"]
                for i in zip(list(total_xp), list(total_xp)[1:]):
                    first = i[0]
                    second = i[1]
                    y.append(abs(total_xp[first] - total_xp[second]))
                if y[-1] < config["minium_xp"]:
                    q += 1
                    g += 1
                    continue
                f = 0
                for xp in total_xp:
                    x.append(f)
                    f += 1
                plt.plot(x, y, label=gwaff[user]["name"].split("#")[0])
                q += 1
                g += 1
            else:
                labelLines(plt.gca().get_lines(), align=True)
                plt.legend(bbox_to_anchor=(1, 1))
                plt.xlabel(
                    f"days since {list(gwaff['408355239108935681']['message_count'].keys())[0].split(' ')}[0]{config['bottom_message']}"
                )
                plt.ylabel("gain")
                title = config["title"]
                if config["minium_xp"] > 0:
                    title += f"\ngain atleast {config['minium_xp']} to appear"
                plt.title(title)
                plt.show()
                plt.close()

                plt.figure(figsize=(14, 7))
                q = 0
        else:
            break
