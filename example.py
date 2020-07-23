import random

n = 10
a = [3, 3, 1, 1, 2, 2, 2, 7, 7, 7]
# # n=int(input())
# # for i in range(n):
# #     x = int(input())
# #     a.append(x)
# for i in range(n):
#   x = random.randint(0,9)
#  a.append(x)
b = 0
c = 0
print(a)
for i in range(n - 1):
    if a[i] == a[i + 1]:  # 1 2 2 2 2
        b = b + 1
    else:
        if b >= 2:
            c += b + 1
        b = 0
if b >= 2:
    c += b + 1
print(c)
