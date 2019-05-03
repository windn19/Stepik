import requests
token = '25730cb4191ea00120df4bbcf6262a1b4a5a8416'
client_id = '11d888eda64382851ce4613ef54889d5607ba22d',
client_secret = '35028eb953e44f81de4e2c861cabf3d6aa8242db'
headers = {
    'Authorization': 'Bearer 25730cb4191ea00120df4bbcf6262a1b4a5a8416'
}
url = 'https://api-ssl.bitly.com/v4/shorten'
options = {
    'long_url': 'https://www.google.com',
    'group_guid': 'dmitry11'
}

res = requests.post(url=url, params=options, headers=headers)
res.encoding = 'utf-8'
print(res.status_code)
print(res)
print(res.json())
