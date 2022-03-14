import requests

CHAMPION_DATA_URL = 'http://ddragon.leagueoflegends.com/cdn/[version_placeholder]/data/en_US/champion.json'
VERSION_LIST_URL = 'https://ddragon.leagueoflegends.com/api/versions.json'

def get_champ_list():
    ver = get_newest_version()
    r = requests.get(CHAMPION_DATA_URL.replace('[version_placeholder]', ver))
    data = r.json()
    output = []
    for key, value in data['data'].items():
        output.append(value['name'])

    return output

def get_newest_version():
    r = requests.get(VERSION_LIST_URL)
    data = r.json()

    return data[0]