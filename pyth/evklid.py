def evklild(a, b):
    if not all([a, b]):
        return max(a, b)
    return evklild(b, a % b)


a, b = map(int, input().split())
print(evklild(a, b))
