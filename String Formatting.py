def print_formatted(number):
    width = len(bin(number)[2:])
    for num in range(1, number + 1):
        print(f"{num:>{width}} {oct(num)[2:]:>{width}} {hex(num).upper()[2:]:>{width}} {bin(num)[2:]:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)