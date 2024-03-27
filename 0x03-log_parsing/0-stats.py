#!/usr/bin/python3
'''refer to readme for question'''

import sys

if __name__ == "__main__":

    def print_stats(file_size, status):
        '''print stats'''
        print("File size: {}".format(file_size))
        for key, value in sorted(status.items()):
            if value != 0:
                print("{}: {}".format(key, value))

    file_size = 0
    status = {"200", "301", "400", "401", "403", "404", "405", "500"}

