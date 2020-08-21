#! /usr/bin/env python3

# https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/

def leastPrimeFactor(n):
    least_prime = [0] * (n+1)

    least_prime[1] = 1

    for i in range(2, n+1):
        if least_prime[i] == 0:
            least_prime[i] = i

        for j in range(2*i, n+1, i):
            if least_prime[j] == 0:
                least_prime[j] = i

    return least_prime[n]

def getFactorization(x):
    factors = []
    while x != 1:
        factors.append(leastPrimeFactor(x))
        x = x // leastPrimeFactor(x)

    return factors

if __name__ == "__main__":
    n = int(input())
    print(getFactorization(n))