import sys

def generate_combinations(digits, max_digit):
    if digits == 0:
        return ['']
    combinations = []
    for i in range(max_digit + 1):
        for combination in generate_combinations(digits - 1, max_digit):
            combinations.append(str(i) + combination)
    return combinations

digit_length = int(sys.argv[1])
choice = int(sys.argv[2])
combo = generate_combinations(digit_length, 9)
start_index = len(combo)*(choice-1)//10
end_index = len(combo)*choice//10

output = "\n".join(combo[start_index:end_index])

# Send output to command terminal
print(output)