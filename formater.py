import requests
import json
same = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php").json()
final  ={}
for i in same['data'] :
    item = {}
    try:
        item['archetype'] = [i['archetype']]
    except :
        item['archetype'] = ["Neutral"]
    try:
        item['type'] = i['type'].lower().split(" ")
    except:
        item['type'] = []
    try:
        item['atk'] = i["atk"]
    except:
        item['atk'] = -2
    try:
        item['def'] = i["def"]
    except:
        item['def'] = -2
    try:
        item['level'] = i["level"]
    except:
        item['level'] = -2
    try:
        item['race'] =  [i['race'].lower()]
    except:
        item['race'] = []
    try:
        item['attribute'] =  [i['attribute'].lower()]
    except:
        item['attribute'] = []
    item["name"] = i['name']
    item['id'] = i['id']
    item["desc"] = i['desc']
    final[str(i['id'])] = item


json.dump(final,open("cards.json",'w'))