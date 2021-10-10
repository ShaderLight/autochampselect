import requests

CHAMPION_DATA_URL = 'http://ddragon.leagueoflegends.com/cdn/11.20.1/data/en_US/champion.json'

def get_champ_list():
    r = requests.get(CHAMPION_DATA_URL)
    data = r.json()
    output = []
    for key, value in data['data'].items():
        output.append(value['name'])

    return output

print(get_champ_list())