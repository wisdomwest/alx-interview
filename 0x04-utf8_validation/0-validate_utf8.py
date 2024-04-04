#!/usr/bin/python3
'''refer to readme'''


def validUTF8(data):
    '''refer to readme'''
    try:
        bytes(data).decode('utf-8')
        return True
    except Exception:
        return False
