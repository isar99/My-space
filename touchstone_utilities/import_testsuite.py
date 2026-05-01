import requests
import yaml
import json

file = "/Users/isarahmad/Downloads/ia-13kg-tc-27-01-2025.yaml"
with open(file, "r") as f:
	yaml_data = f.read()
print(yaml_data)

#single_line_yaml = yaml.dump(yaml_data, default_flow_style=True)

resp1 = requests.post("https://qa.voereir.io/api/v2/login", json={"login": "qa", "passwd": "test123"})
resp1_json = resp1.json()

token = resp1_json["token"]
team_uuid = resp1_json["user"]["team"]["uuid"]

headers = {"token": token, "team": team_uuid}
resp2 = requests.post("https://qa.voereir.io/api/v2/import/testsuite?format=yaml", headers=headers, data=yaml_data)

print(resp2.json())
