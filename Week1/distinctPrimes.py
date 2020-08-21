#! /usr/bin/env python3
# Star
# https://www.spoj.com/problems/AMR11E/

n = 2700
p = [0] * (n+1)
for i in range(2,n+1):
    if p[i] == 0:
        # Below for loop is for getting multiples of i (i*1=1;i*2=2i...)
        for j in range(i*2,n+1,i):
            p[j] += 1

arr = [0] * 1001
i, j = 30, 1
while i < 2700 and j < 1001:
    if p[i] >= 3:
        arr[j] = i
        j+=1
    i += 1

t = int(input())
x = []
for i in range(t):
    n = int(input())
    x.append(n)

for i in x:
    print(arr[i])