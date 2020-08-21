#! /usr/bin/env python3

# https://www.hackerrank.com/challenges/power-of-large-numbers/problem

x, y = input().split()
x, y = int(x), int(y)
print(pow(x, y, (10**9 + 7)))