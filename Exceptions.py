if __name__ == "__main__":
    test_case_count = int(input())
    number_pairs = []

    for _ in range(test_case_count):
        pair = input().split()
        number_pairs.append(pair)

    for pair in number_pairs:
        try:
            numerator = int(pair[0])
            denominator = int(pair[1])
            result = numerator // denominator
            print(result)
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as e:
            print("Error Code:",e)

