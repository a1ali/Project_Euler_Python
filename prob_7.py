

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# Changed it to find me palindrome primes change the nested if below to bring back original

import math
primes = []

i = 2


def palincheck(x):
    palindrom = False
    list_p = [int(x) for x in str(x)]
    new_p = list_p.copy()
    new_p = new_p[::-1]

    if new_p == list_p:
        palindrom = True

    return palindrom


def isPrime(x):
    for divisor in range(2, x):
        if x % divisor == 0:
            # X is non-prime
            return False

    return True


while len(primes) < 10001:
    if isPrime(i):
        if palincheck(i):
            primes.append(i)
            print('#: {} , P: {}'.format(len(primes), i))

    i += 1


#: 10001 , P: 104743
# 100th palindrome prime 94049