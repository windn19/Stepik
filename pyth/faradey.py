from matplotlib import pyplot as plt
import time


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        acc = min(acc, time.perf_counter() - t0)

    return acc


def compare(fs, args):
    xs = list(range(len(args)))
    for f in fs:
        plt.plot(xs, [timed(f, chunk) for chunk in args],
                 label=f.__name__)
    plt.legend()
    plt.grid(True)


def compare1(args):
    plt.plot([chunk for chunk in range(args)])
    plt.legend()
    plt.grid(True)


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


def far3(n):
    sum = 1
    num = 1
    for i in range(2, n):
        num, sum = sum, (sum + num) % 10
    return sum


def fab(n):
    sum = 1
    num = 0
    a = [0, 1]
    for i in range(2, 60):
        num, sum = sum, (sum + num) % 10
        a.append(sum)
    print(a)
    return a[n % 60]


compare1(20)
