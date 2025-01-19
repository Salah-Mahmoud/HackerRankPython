if __name__ == "__main__":
    n = int(input())
    for i in range(1, n + 1):
        increasing = ''.join(str(x) for x in range(1, i + 1))
        decreasing = ''.join(str(y) for y in range(i - 1, 0, -1))
        print(increasing + decreasing)
