def is_lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True

count = 0
for n in range(1, 10000):
    if is_lychrel(n):
        count += 1

print(count)
