# Easy sol
def mutate_string(string, position, character):
    result = []
    for index, char in enumerate(string):
        if index==position:
            char = character
            result.append(char)
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Creative Solution
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

