if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        command = input().split()
        action = command[0]

        if action == 'insert':
            result.insert(int(command[1]), int(command[2]))
        elif action == 'remove':
            result.remove(int(command[1]))
        elif action == 'print':
            print(result)
        elif action == 'append':
            result.append(int(command[1]))
        elif action == 'sort':
            result.sort()
        elif action == 'pop':
            result.pop()
        elif action == 'reverse':
            result.reverse()
