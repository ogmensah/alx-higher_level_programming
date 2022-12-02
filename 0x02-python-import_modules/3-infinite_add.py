#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    t = 0
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            t += int(arg)
    print(t)
