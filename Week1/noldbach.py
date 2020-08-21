#! /usr/bin/env python3
# https://codeforces.com/problemset/problem/17/A?locale=en

n, k = input().split()
n = int(n)
k = int(k)
p = [True] * (n+1)
p[0] = p[1] = False
primes = []
count = 0

for i in range(2, n+1):
    if p[i]:
        if i**2 <= n:
            for j in range(i**2, n+1, i):
                p[j] = False
        primes.append(i)

# print(primes)

for i in range(len(primes)-1):
    if primes[i] == 2:
        count += 1
    elif (primes[i] + primes[i+1] + 1) in primes:
        count += 1

if count >= k:
    print("YES")
else:
    print("NO")