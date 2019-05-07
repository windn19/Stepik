import requests
token = '25730cb4191ea00120df4bbcf6262a1b4a5a8416'
client_id = '11d888eda64382851ce4613ef54889d5607ba22d',
client_secret = '35028eb953e44f81de4e2c861cabf3d6aa8242db'
headers = {
    'Authorization': 'Bearer 25730cb4191ea00120df4bbcf6262a1b4a5a8416',
    'Content-Type': 'application/json'
}
url = 'https://api-ssl.bitly.com/v4/shorten'
options = {
    'long_url': 'https://realpython.com/python-request',
    "group_guid": "Bj4uewAKgEY"
}

res = requests.post(url=url, headers=headers, json=options)
print(res.status_code)
print(res)
print(res.json())
print(res.json()['link'])
# {'groups': [{'created': '2019-04-30T14:27:00+0000', 'modified': '2019-04-30T14:27:00+0000',
# 'bsds': [], 'guid': 'Bj4uewAKgEY', 'organization_guid': 'Oj4ueen4Zub', 'name': 'dmitry11',
# 'is_active': True, 'role': 'org-admin', 'references':
# {'organization': 'https://api-ssl.bitly.com/v4/organizations/Oj4ueen4Zub'}}]}