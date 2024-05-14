#!/usr/bin/python3
'''refer to the README.md file for the problem statement'''


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        n = nums[i]
        primes = [i for i in range(1, n + 1) if is_prime(i)]

        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
