import requests
from yaml import safe_load


def get():
    with open("config.yml", "r") as file:
        config = safe_load(file)
    page = 0
    users = {}
    q = 0
    i = 0
    while i < int(config["data_range"] / 100):
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
        i += 1
    return users
