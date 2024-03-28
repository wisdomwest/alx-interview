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
    found = {}
    status = {"200", "301", "400", "401", "403", "404", "405", "500"}
    count = 0

    try:
        for line in sys.stdin:
            try:
                word = line[:-1].split()

                size = int(word[-1])
                file_size += size

                code = int(word[-2])
                if str(code) in status:
                    found[str(code)] = found.get(str(code), 0) + 1

            except BaseException:
                pass

            count += 1

            if count % 10 == 0:
                print_stats(file_size, found)

    except KeyboardInterrupt:
        print_stats(file_size, found)
        raise

    print_stats(file_size, found)
