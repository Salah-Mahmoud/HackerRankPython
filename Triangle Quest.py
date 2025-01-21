if __name__ == "__main__":
    n = int(input())
    for i in range(1, n):
        for x in range(1, i + 1):
            print(i, end="")
        print()
