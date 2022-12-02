#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        for n, arg in enumerate(sys.argv[1:], start=1):
            print(f"{n:d}: {arg}")
