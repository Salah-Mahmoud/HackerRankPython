from itertools import permutations

if __name__ == "__main__":
    w, n = input().split()
    for i in permutations(sorted(w), int(n)):
        print("".join(i))
