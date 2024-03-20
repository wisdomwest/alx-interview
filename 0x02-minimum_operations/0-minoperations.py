#!/usr/bin/python3
'''Module for minOperations'''


def minOperations(n):
    '''check readme for more information'''
    if n <= 1:
        return 0
    for x in range(2, n+1):
        if n % x == 0:
            return minOperations(int(n/x)) + x
