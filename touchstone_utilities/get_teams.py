##############################################################################
# Copyright (c) 2022-present VoerEir AB - All Rights Reserved                #
# Unauthorized copying of this file, via any medium is strictly prohibited   #
# Proprietary and confidential                                               #
# Written by Isar Ahmad <isar@voereir.com>, Sep 2024                         #
##############################################################################

"""
File to list teams (as name and UUID dict) present in QA or VM by providing
URL, username, password
"""

import requests
import sys

# Fetch the arguments
URL = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]

# Login into QA
if "/api/v2" in URL:
    response = requests.post(URL+"/login",
                         json={"login": username, "passwd": password},
                         verify=False)
elif "/api/v3" in URL:
    response = requests.post(URL+"/auth",
                         json={"login": username, "passwd": password, "authType": "BUILTIN"},
                         verify=False)

data = response.json()
# Capture tteam uuid  and  name
mylist = []
for each_Team in data["teams"]:
        teams_dict = {}
        teams_dict[each_Team['name']] = each_Team['uuid']
        mylist.append(teams_dict)
print(mylist)
