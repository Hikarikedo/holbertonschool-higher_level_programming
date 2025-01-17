#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Exclude the script name and cast arguments to integers, summing them
    result = sum(int(arg) for arg in sys.argv[1:])
    print(result)
