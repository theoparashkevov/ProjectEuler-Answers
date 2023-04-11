
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen


def main():
    """Maximum path sum II"""

    # Constants
    URL = 'https://projecteuler.net/project/resources/p067_triangle.txt'

    # Prepare triangle
    triangle = [[int(i) for i in line.split()] for line in urlopen(URL)]

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    print(triangle[0][0])

if __name__ == '__main__':
    main()