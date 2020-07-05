import json


def generate(new_users, time):
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
