def fibb(n, m):
    period = [60, 300, 1500, 15000, 150000]
    sum = 1
    num = 0
    a = [1]
    r = len(m)
    for i in range(2, period[r-1]+1):
        num, sum = sum, (sum + num) % 10**r
        a.append(sum)
    print(a)
    print(len(a))
    print(period[r-1])
    print(int(n) % period[r-1])
    return a[(int(n) % period[r-1])-1]


n, m = map(str, input().split())
z = fibb(n, m)
print(z)
print(z % int(m))
