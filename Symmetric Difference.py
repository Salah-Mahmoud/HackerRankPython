if __name__ == "__main__":
    m = int(input())
    a = input().split()
    n = int(input())
    b = input().split()

    diff1 = set(a) - set(b)
    diff2 = set(b) - set(a)
    result = diff1.union(diff2)

    print("\n".join(map(str, sorted(map(int, result)))))
