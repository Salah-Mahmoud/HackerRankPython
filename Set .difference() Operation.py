if __name__ == "__main__":
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    diff = a - b
    print(len(diff))
