import requests
import json

resp1 = requests.post("https://qa.voereir.io/api/v2/login", json={"login": "qa", "passwd": "test123"}, headers={"Content-type": "application/json", "team": "553ccbd0-c300-11e6-812a-766d78a9d835"})

resp1_json = resp1.json()

get_token = resp1_json["token"]
get_team = resp1_json["user"]["team"]["uuid"]
get_user = resp1_json["user"]["uuid"]

headers = {"token": get_token, "team": get_team}

resp3 = requests.get(f"https://qa.voereir.io/api/v2/test_cases?available=true&filter=test_area&filter=origination&filter=is_background&filter=context_uuid&filter_value=nfvi_performance&filter_value=clone&filter_value=false&filter_value=3cf2d6d8-d2db-11e9-aa1d-0c54158d22b9", headers=headers)


params1 = {
    "available": "true",
    "filter": ["created_by", "test_area", "origination", "is_background", "context_uuid"],
    "filter_value": [get_user, "nfvi_performance", "clone", "false", "3cf2d6d8-d2db-11e9-aa1d-0c54158d22b9"]
}


resp4 = requests.get(f"https://qa.voereir.io/api/v2/test_cases", params=params1, headers=headers)

print(resp4.json())

print(resp4.json()["count"])
