#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("Python Main")
    print(f"Argument Count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument: {i:>6}: {arg}")
