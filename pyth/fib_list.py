def fibb(n, m):
    sum = 1
    num = 0
    for i in range(2, piz):
        num, sum = sum, (sum + num) % m
        a.append(sum)


# [0, 1, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5, 4, 2, 6, 1,
# 0, 1, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5, 4, 2, 6, 1,
# 0, 1, 1, 2, 3, 5, 1, 6, 0, 6
a = [0, 1]
n, m = map(int, input().split())
piz = m * 6
fibb(n, m)
print(a)
word = a[:2]
c = a.count(word)
# k = a.index(word, len(word)-1)
print(word, c)
# mas = ''
# for i in a:
#     mas += str(i)
# word = str(a[0])
# c = mas.count(word, m)
# k = mas.index(word, len(word)-1)
# print(word, mas, c, k)
# for i in range(1, len(a)-1):
#     print(i)
#     word += str(a[i])
#     if mas.count(word, i) <= 2:
#         k = mas.index(word, i)
#         break
#     print(mas.count(word, i))
# word = mas[:k]
# print(word)
# t = ''
# for i in range(len(a)):
#     t += str(a[i])
#     if t == word:
#         print('k=', i)
#         break
# print(k)
# print(a[:i+1])
