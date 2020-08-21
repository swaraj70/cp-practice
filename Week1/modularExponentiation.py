#! /usr/bin/env python3
# Star
# http://nadide.github.io/Modular-Exponentiation/

def modulo(x, y, m):
    if y == 0:
        print(1)

    x = x % m
    res = 1
    while y > 0:
        if (y % 2):
            res = (res * x) % m

        x = (x * x) % m
        y = y/2

    print(res)

if __name__ == "__main__":
    x, y, m = input().split()
    x, y, m = int(x), int(y), int(m)
    modulo(x, y, m)
    