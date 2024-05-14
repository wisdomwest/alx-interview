#!/usr/bin/python3
'''refer to the README.md file for the problem statement'''


def isWinner(x, nums):
    '''get won by the player'''
    maria = 0
    ben = 0

    for n in nums:
        rounds = list(range(1, n + 1))
        prime = prime_count(rounds)

        if not prime:
            ben += 1
            continue

        marias = True

        while(True):
            if not prime:
                if marias:
                    ben += 1
                else:
                    maria += 1
                break

            smallest = prime.pop(0)
            rounds.remove(smallest)

            for x in rounds:
                if x % smallest == 0:
                    rounds.remove(x)

            marias = not marias

    if maria == ben:
        return None
    if maria > ben:
        return "Maria"

    return "Ben"


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_count(rounds):
    primes = []
    for num in rounds:
        if is_prime(num):
            primes.append(num)
    return primes
