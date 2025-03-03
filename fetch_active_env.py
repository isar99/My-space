##############################################################################
# Copyright (c) 2022-present VoerEir AB - All Rights Reserved                #
# Unauthorized copying of this file, via any medium is strictly prohibited   #
# Proprietary and confidential                                               #
# Written by Md Safiyat Reza <safiyat@voereir.com>, Oct 2023                 #
##############################################################################

"""
File to list environments present in QA or VM by providing
URL, username, password, team (team name and uuid)
"""

import requests
import sys
import json

# Pass the base URL
cloud_type = sys.argv[1]
base_url= sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
team = sys.argv[5]

team = team.replace("'","")
teams= json.loads(team)
team = list(teams.items())[0][1]

# Login into QA
if "/api/v2" in base_url:
    response = requests.post(base_url+"/login",
                         json={"login": username, "passwd": password},
                         verify=False)
    # Get token in V2 API and add to headers
    data = response.json()
    token = data["token"]
    headers = {'token': token, 'team':team}
elif "/api/v3" in base_url:
    response = requests.post(base_url+"/auth",
                         json={"login": username, "passwd": password, "authType": "BUILTIN"},
                         verify=False)
    # Get cookie in v3 API and add to headers
    for cookie in response.cookies:
        resp_cookie = f"{cookie.name}={cookie.value}"
    headers = {'cookie': resp_cookie, 'team':team}

# Call the Get Request to fetch active environment List
params = {'filter': 'status', 'filter_value': 'active'}
url = base_url+"/"+cloud_type+"/environments"
response = requests.get(url, headers=headers, params=params, verify=False)
data = response.json()
mylist = []
for each in data['items']:
        mylist.append(each['name'])
print(mylist)
