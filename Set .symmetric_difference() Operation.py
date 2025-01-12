if __name__ == "__main__":
    n = int(input())
    x = set(map(int, input().split()))
    m = int(input())
    y = set(map(int, input().split()))
    diff = x ^ y
    print(len(diff))
