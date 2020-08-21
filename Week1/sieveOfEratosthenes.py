#! /usr/bin/env python3

# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

n = int(input())
p = [True] * (n+1)
p[0] = p[1] = False
for i in range(2,n+1):
    if p[i]:
        if i**2 <= n:
            for j in range(i**2,n+1,i):
                p[j] = False

for i in range(len(p)):
    if p[i]:
        print(i)