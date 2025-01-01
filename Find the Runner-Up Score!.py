if __name__ == '__main__':
    n = int(input())
    a = list(set(map(int, input().split())))
    a.sort(reverse=True)
    print(a[1])
