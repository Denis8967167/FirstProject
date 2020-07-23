def Xor(a, b):
    if a != b:
        return True
    if a == b:
        return False


a = input()
b = input()

res = Xor(a, b)
print(res)

