if __name__=="__main__":
    n1 = input()
    x = set(input().split())
    n2 = input()
    y = set(input().split())
    print(len(x.intersection(y)))