def far(n):
    a = [0, 1]
    for i in range(2, n):
        a.append(a[i-2] + a[i-1])
    print(a)
    print(len(a))
    return a[n-1]


def far1(n):
    if n <= 1:
        return n
    else:
        return far1(n-2) + far1(n-1)


def far2(n):
    sum = 1
    num = 0
    for i in range(2, n):
        num, sum = sum, sum + num
    return sum
# 218922995834555169026


n = int(input())
print(far2(n))
