import urllib.request
import xmltodict
from pprint import pprint
# Ежедневные курсы валют ЦБ РФ
# url = 'https://www.cbr-xml-daily.ru/daily_json.js'
#
# res = requests.get(url)
# print(res.status_code)
# data = res.json()
# print(data['Valute']['USD']['Previous'])
# data = res.read()
# data1 = '20/12/2018'
# data2 = '22/12/2018'
# url = f"http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={data1}&date_req2={data2}&VAL_NM_RQ=R01235"
# # Чтение URL
# webFile = urllib.request.urlopen(url)
#
# data = webFile.read()
# #
# # # Имя файла
# # # UrlSplit = url.split("/")[-1]
# # # ExtSplit = UrlSplit.split(".")[1]
# # # FileName = UrlSplit.replace(ExtSplit, "xml")
# #
# with open('new.xml', "wb") as localFile:
#     localFile.write(data)
#
# webFile.close()

with open('new.xml', mode='r') as f:
    xml = f.read()
mydict = xmltodict.parse(xml)
pprint(mydict['ValCurs']['Record'][0]['@Date'])