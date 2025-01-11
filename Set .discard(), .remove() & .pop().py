if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        c = input().split()
        if c[0] == "pop":
            if s:
                s.remove(min(s))
        elif c[0] == "remove":
            try:
                s.remove(int(c[1]))
            except KeyError:
                pass
        elif c[0] == "discard":
            s.discard(int(c[1]))
    print(sum(s))
