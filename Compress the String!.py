from itertools import groupby

input_string = input()

result = [(len(list(group)), int(key)) for key, group in groupby(input_string)]

formatted_output = " ".join(f"({count}, {char})" for count, char in result)

print(formatted_output)
