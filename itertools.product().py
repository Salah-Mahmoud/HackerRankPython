if __name__ == '__main__':
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    result = [(i, j) for i in x for j in y]
    print(*result, end="")