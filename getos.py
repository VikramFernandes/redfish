import requests
import json
import pprint

username = "Administrator"
password = ""
ilo = ""

# connect
url = "https://" + ilo + "/redfish/v1/SessionService/Sessions"

auth_token = None
url = "https://" + ilo + "/redfish/v1/SessionService/Sessions/"
headers = {"Content-Type": "application/json"}


payload = {
        "UserName": username,
        "Password": password
    }
auth = requests.post(url,
                    data=json.dumps(payload),
                    headers=headers,
                    verify=False)

if auth.status_code != 201:
    try:
        answer = auth.json()
    except ValueError:
        answer = ""

auth_token = auth.headers.get("x-auth-token")
print("X-Auth-Token : " + auth_token)

resource = "/redfish/v1/Systems/1/"
#resource = "/redfish/v1/Systems/1/Oen/Hpe/HostOs"
url = "https://" + ilo + resource

header = {"Content-Type": "application/json","X-Auth-Token": auth_token }

retObj = requests.get(url, headers=header, verify=False)

#print(json.dumps(retObj.json(), indent=4))

hostOS = retObj.json()
hostOS2 = hostOS['Oem']['Hpe']['HostOS']

pprint.pprint(hostOS2)
