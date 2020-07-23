n = int(input())

b = 'prime'

for i in range(2, n):
    if n % i == 0:
        b = 'compositive'
print(b)
