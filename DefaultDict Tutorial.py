from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    group_a = []
    group_b = []

    for _ in range(n):
        group_a.append(input().strip())
    for _ in range(m):
        group_b.append(input().strip())

    index_map = defaultdict(list)
    for i, word in enumerate(group_a):
        index_map[word].append(i + 1)
    for word in group_b:
        if word in index_map:
            print(" ".join(map(str, index_map[word])))
        else:
            print(-1)  