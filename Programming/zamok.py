from pprint import pprint
from itertools import permutations


def gen_numeric():
    data = []
    a = set()
    b = set()
    for i in range(5, 21):
        if i not in a and i not in b:
            a.add(i)
            for j in range(5, 21):
                if j not in a and j not in b:
                    a.add(j)
                    for k in range(5, 21):
                        if k not in a and k not in b:
                            a.add(k)
                            for m in range(5, 21):
                                if m not in a and m not in b:
                                    a.add(m)
                                    if i+j+k+m == 50:
                                        data.append([i, j, k, m])
                                        a |= {i, j, k, m}
                                        if len(data) > 4:
                                            yield data
                                            data = []
                                    a.remove(m)
                            a.remove(k)
                    a.remove(j)
            a.remove(i)


def gen_kol(mas):
    data = []
    for i in range(4):
        if mas[0][i] + mas[1][i] + mas[2][i] + mas[3][i] == 50:
            data.append([mas[0][i], mas[1][i], mas[2][i], mas[3][i]])
            pprint(data)
            if not len(data) % 4:
                yield data
                data = []


a = set()
b = []
data = list(filter(lambda x: sum(x) == 50, list(permutations(range(5, 21), 4))))
for num, i in enumerate(data):
    for k in i:
        a.add(k)
    
    b.append(list(i))
    if (num+1) % 4 == 0:
        print(b)
        print(len(a))
        b = []
        a = set()