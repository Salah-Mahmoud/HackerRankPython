from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    e = list(map(int, input().split()))
    room_count = defaultdict(int)

    for room in e:
        room_count[room] += 1

    for room, count in room_count.items():
        if count == 1:
            print(room)
            break
