def a(a):
    if a == a[::-1]:
        return True
    else:
        return False
print(a(input()))