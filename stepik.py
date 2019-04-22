import json

d = {}
d1 = {}
c = set()
b = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []},' \
    ' {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'
a = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
di = '[{"name": "A", "parents": ["B", "C", "D"]},{"name": "E", "parents": ["F", "G"]},' \
     '{"name": "I", "parents": ["E", "F", "Y", "D", "G"]},{"name": "B", "parents": ["I", "Y", "D", "G"]},' \
     '{"name": "F", "parents": ["D", "Z"]},{"name": "C", "parents": ["Y", "G", "Z"]},{"name": "Y", "parents": []},' \
     '{"name": "D", "parents": []},{"name": "G", "parents": ["Y", "D"]},{"name": "Z", "parents": ["D", "G"]}]'
strings = '[{"name": "dfgre", "parents": ["gsdfgre"]},' \
          ' {"name": "hsdgreg", "parents": ["dfgre", "gsd"]},' \
          ' {"name": "gsd", "parents": ["dfgre"]},' \
          ' {"name": "gsdfgre", "parents": []}] '


def predok(m, mass):
    for i in mass:
        d1[i] = d1.get(i, 0) + 1
        predok(i, d[i])


reada = json.loads(di)
print(reada)
for i in reada:
    d[i['name']] = i['parents']
print(d)
for i in d:
    d1[i] = d1.get(i, 0)+1
    predok(i, d[i])

for i, num in sorted(d1.items()):
    print(i, ":", num)
# A : 5
# B : 1
# C : 4
# D : 2
# E : 1
# F : 3
