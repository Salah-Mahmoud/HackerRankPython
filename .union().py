if __name__ == "__main__":
    n = input()
    x = list(map(int, input().split()))
    m = input()
    y = list(map(int, input().split()))
    print(len(set(x + y)))
