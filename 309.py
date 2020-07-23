def election(x, y, z):
    if a != b and a != c:
        return b
    if b != a and b != c:
        return a
    if c != a and c != b:
        return a


a = 1
b = 0
c = 1
res = election(a, b, c)
print(res)
