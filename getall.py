
from api import api

ops_api = api.Api()
logged_in = ops_api.login()

filters = {
    "version": 6,
    "name": "",
    "vehicles": {},
    "weaponClasses": {},
    "slots": {
        "oneToFive": "on",
        "sixToTen": "on",
        "tenPlus": "on",
        "none": "on",
    },
    "regions": {
        "EU": "off",
        "Asia": "off",
        "NAm": "off",
        "SAm": "off",
        "AU": "off",
        "OC": "off"
    },
    "kits": {},
    "misc": {},
    "scales": {}
}


def region_players(region):
    region_filters = {**filters, "regions": {**filters["regions"], f"{region}": "on"}}
    s, solider_a, que_a, spectator_a = count_players(region_filters)
    print("Region: ", region)
    print("Server amount: ", s)
    print("Total soliders: ", solider_a)
    print("Total in que: ", que_a)
    print("Total spectators: ", spectator_a)


def count_players(r_filters):
    servers = ops_api.pc.search_servers(r_filters)["result"]["gameservers"]
    solider_amount = 0
    que_amount = 0
    spectator_amount = 0
    for server in servers:
        solider_amount += server["slots"]["Soldier"]["current"]
        que_amount += server["slots"]["Queue"]["current"]
        spectator_amount += server["slots"]["Spectator"]["current"]
    return len(servers), solider_amount, que_amount, spectator_amount


if logged_in:
    region_players("OC")
    region_players("EU")
    region_players("NAm")
    region_players("SAm")
    region_players("AU")
    region_players("Asia")
else:
    print("Cookie is invalid")
