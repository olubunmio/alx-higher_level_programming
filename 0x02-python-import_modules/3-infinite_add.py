#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ac = len(sys.argv) - 1
    if ac == 0:
        print('0')
        sys.exit()
    sum = 0
    for i in range(1, len(sys.argv)):
        sum = sum + int(sys.argv[i])

    print("{:d}".format(sum))
