

def is_pentagonal(p):
    """function to check if the
    given number is pentagonal"""
    if (1+(24*p+1)**0.5) % 6 == 0:
        return True
    return False


def is_hexagonal(h):
    """function to check if the
    given number is hexagonal"""
    if (1+(8*h+1)**0.5) % 4 == 0:
        return True
    return False

# iterator start after 285
i = 286

# while loop for iterating
while True:
    triangle = i*(i+1)/2
    if is_pentagonal(triangle) and is_hexagonal(triangle):
        print(triangle)
        break
    i += 1
