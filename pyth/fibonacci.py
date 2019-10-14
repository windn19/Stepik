def fibb(n, m):
    a = [0, 1]
    sum, num, piz = 1, 0, m*6
    for i in range(2, piz):
        num, sum = sum, (sum + num) % m
        a.append(sum)
    print(a)
    first, second, third = 0, 1, 1
    for i in range(5, len(a) - 1):
        if a[i] == third and a[i - 1] == second and a[i - 2] == first:
            break
    a = a[:i-2]
    print(a)
    border = len(a)
    return a[n % border]


def far2(n):
    sum = 1
    num = 0
    for i in range(2, n+1):
        num, sum = sum, sum + num
        fib.append(sum)


def key(ar):
    # mas = ''
    # for i in a:
    #     mas += str(i)
    # word = str(a[:1])
    # for i in range(1, len(a) - 1):
    #     word += str(a[i])
    #     if mas.count(word, i) <= 2:
    #         try:
    #             k = mas.index(word, i)
    #         except ValueError:
    #             k = len(a)-1
    #         break
    # word = mas[:k]
    # t = ''
    # for i in range(len(a)):
    #     t += str(a[i])
    #     if t == word:
    #         break
    first = 0
    second = 1
    third = 1
    for i in range(5, len(a)-1):
        if a[i] == third and a[i-1] == second and a[i-2] == first:
            break
    return a[:i-2]


n, m = map(int, input().split())
#far2(n)
print(fibb(n, m))
# keys = key(a)
# print(keys)
# border = len(keys)
# print(a[n % border])
# for i in range(n):
#     border = len(keys)
#     print(border, i, i % border, a[i % border])
#     print(f'{fib[i]} -- {fib[i] % m} -- {a[i % border]}')
# n = far2(n)
# print(n)
# print(n % m) [0, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5, 4, 2, 6, 1, 0, 1, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5, 4, 2, 6, 1, 0, 1, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5]

