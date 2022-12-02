#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        a = 's'
        if len(sys.argv) == 2: a = ''
        print(f"{len(sys.argv) - 1} argument{a:s}:")
        for n, arg in enumerate(sys.argv[1:], start=1):
            print(f"{n:d}: {arg}")
