import requests
import json

parameters = {
    "lat": 40.71,
    "lon": -74
}

res = requests.get("https://api.open-notify.org/iss-pass.json")

print(res)

# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# jprint(res.json())