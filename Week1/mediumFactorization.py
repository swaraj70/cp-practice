#! /usr/bin/env python3

# https://www.spoj.com/problems/FACTCG2/

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
    factors = ''
    while x != 1:
        factors += str(leastPrimeFactor(x))
        x = x // leastPrimeFactor(x)

    return factors

if __name__ == "__main__":
    n = int(input())
    if n == 1:
        print('1\n')
    else:
        print('1 x ' + ' x '.join(getFactorization(n)))