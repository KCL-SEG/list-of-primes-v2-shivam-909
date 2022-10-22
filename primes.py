"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""




import math
def primes(number_of_primes):
    list = []

    i = 1
    while len(list) != number_of_primes:
        if is_prime(i):
            list.append(i)
        i = i + 1
    return list


def is_prime(n):
    for i in range(1, int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True
