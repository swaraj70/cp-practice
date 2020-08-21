#! /usr/bin/env python3

# https://wiki.haskell.org/99_questions/Solutions/39

def primeRange(l,h):
    p = [True] * (h+1)
    p[0] = p[1] = False
    for i in range(2,h+1):
        if p[i]:
            if i**2 <= h:
                for j in range(i**2,h+1,i):
                    p[j] = False

    for i in range(l,h+1):
        if p[i]:
            print(i)

if __name__ == "__main__":
    l, h = input().split()
    l = int(l)
    h = int(h)
    primeRange(l,h)
    