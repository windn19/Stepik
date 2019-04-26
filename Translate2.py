import requests

urlAPI = 'https://api.mymemory.translated.net/get'

par = {
    'q': 'Wolf, meeting with a Lamb astray from the fold,'
         "resolved not to lay violent hands on him, but to find some plea"
         " to justify to the Lamb the Wolf's right to eat him",
    'langpair': 'en|ru'
}

res = requests.get(url=urlAPI, params=par)
res.encoding = 'utf-8'
data = res.json()
print(data)
print
print(data['responseData']['translatedText'])
