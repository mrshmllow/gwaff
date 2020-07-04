import requests
import json
import matplotlib.pyplot as plt
import matplotlib as mpl
from labellines import labelLines


def gethistory():
    r0 = requests.get("https://mee6.xyz/api/plugins/levels/leaderboard/377946908783673344").json()
    r1 = requests.get("https://mee6.xyz/api/plugins/levels/leaderboard/377946908783673344?page=1").json()
    r2 = requests.get("https://mee6.xyz/api/plugins/levels/leaderboard/377946908783673344?page=2").json()

    users = {

    }
    i = 0
    for user in r0["players"]:
        users[str(i)] = user
        i += 1
    for user in r1["players"]:
        users[str(i)] = user
        i += 1
    for user in r2["players"]:
        users[str(i)] = user
        i += 1

    return users


def makegwaff(new_users, time):
    with open("gwaff.json") as json_file:
        gwaff = json.load(json_file)
        json_file.close()

    for user in new_users:
        if new_users[user]["id"] not in gwaff:
            gwaff[new_users[user]["id"]] = {
                "name": f"{new_users[user]['username']}#{new_users[user]['discriminator']}",
                "message_count": {
                    str(time): new_users[user]["message_count"]
                },
                "total_xp": {
                    str(time): new_users[user]["xp"],
                },
                "detailed_xp": {
                    str(time): new_users[user]["detailed_xp"]
                },
                "level": {
                    str(time): new_users[user]["level"]
                }
            }
        else:
            gwaff[new_users[user]["id"]]["name"] = f"{new_users[user]['username']}#{new_users[user]['discriminator']}"
            gwaff[new_users[user]["id"]]["message_count"][str(time)] = new_users[user]["message_count"]
            gwaff[new_users[user]["id"]]["total_xp"][str(time)] = new_users[user]["xp"]
            gwaff[new_users[user]["id"]]["detailed_xp"][str(time)] = new_users[user]["detailed_xp"]
            gwaff[new_users[user]["id"]]["level"][str(time)] = new_users[user]["level"]

    return gwaff


def xpgained(gwaff):
    colours = ["#ff1500", "#fffb00", "#2fff00", "#00ffff", "#0044ff", "#a200ff", "#ff00c8"]

    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=['blue', 'green', 'red', 'cyan', 'magenta',
                                                        'yellow', 'black', 'purple', 'pink',
                                                        'brown', 'orange', 'teal', 'coral',
                                                        'lightblue', 'lime', 'lavender',
                                                        'turquoise', 'darkgreen', 'tan', 'salmon',
                                                        'gold'])

    plt.style.use('dark_background')

    plt.figure(figsize=(14, 7))
    q = 0
    for user in gwaff:
        if q < 19:
            y = [0]
            x = []
            total_xp = gwaff[user]["total_xp"]

            for i in zip(list(total_xp), list(total_xp)[1:]):
                first = i[0]
                second = i[1]
                y.append(abs(total_xp[first] - total_xp[second]))

            print(y)
            print(y[-1])
            if y[-1] < 500:
                print(f"{gwaff[user]['name'].split('#')[0]} skipped")
                q += 1
                continue

            print("passed")

            f = 0
            for xp in total_xp:
                x.append(f)
                f += 1

            line = plt.plot(x, y, label=gwaff[user]["name"].split("#")[0])
        q += 1

    labelLines(plt.gca().get_lines(), align=True)
    plt.legend(bbox_to_anchor=(1, 1))
    plt.xlabel(f"days since {list(gwaff['408355239108935681']['message_count'].keys())[0].split(' ')[0]}\n\nJoin cremes server for dedicated gwaff channel.\nCheck out the github on bwac2517/gwaff")
    plt.ylabel("gain")
    plt.title("GWAFF V2\nxp gain overtime (top 20)\ngain atleast 500 xp to appear")
    plt.show()
    plt.close()

    plt.figure(figsize=(14, 7))
    q = 0
    for user in gwaff:
        if 40 > q > 19:
            y = [0]
            x = []
            total_xp = gwaff[user]["total_xp"]
            for i in zip(list(total_xp), list(total_xp)[1:]):
                first = i[0]
                second = i[1]
                y.append(abs(total_xp[first] - total_xp[second]))
            print(y)
            print(y[-1])
            if y[-1] < 500:
                print(f"{gwaff[user]['name'].split('#')[0]} skipped")
                q += 1
                continue

            f = 0
            for xp in total_xp:
                x.append(f)
                f += 1
            line = plt.plot(x, y, label=gwaff[user]["name"].split("#")[0])
        q += 1
    labelLines(plt.gca().get_lines(), align=True)
    plt.legend(bbox_to_anchor=(1, 1))
    plt.title("GWAFF V2\nxp gain overtime (top 20 - 40)\ngain atleast 500 xp to appear")
    plt.xlabel(f"days since {list(gwaff['408355239108935681']['message_count'].keys())[0].split(' ')[0]}\n\nJoin cremes server for dedicated gwaff channel.\nCheck out the github on bwac2517/gwaff")
    plt.ylabel("gain")
    plt.show()
