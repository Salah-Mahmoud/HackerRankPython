import math
import os
import random
import re
import sys


def solve(s):
    result = []
    for w in s.split(" "):
        if w:
            if w[0].isdigit():
                result.append(w)
            else:
                result.append(w.capitalize())
        else:
            result.append("")
    return " ".join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
