# Counts the number of digits until the first non-digit
def count_digits(string):
    for i in range(len(string)):
        if not string[i].isdigit():
            return i
    return float.inf



with open('input.txt', 'r') as f:
    instruction_string = f.read().strip()

total = 0
do_instruction = True

for i in range(len(instruction_string)):
    if do_instruction:
        if instruction_string[i:i + 4] == 'mul(': # Checks for 'mul(' at the start
            digit_number_one = count_digits(instruction_string[i + 4:]) # Counts how many digits are in the first number 
            if digit_number_one < 4 and digit_number_one > 0 and instruction_string[i + 4 + digit_number_one] == ',': # If number is within allowed length, and followed by a ','
                number_one = int(instruction_string[i + 4:i+ 4 + digit_number_one]) # Sets variable number_one to the first number in the mul
                digit_number_two = count_digits(instruction_string[i + 5 + digit_number_one:]) # Counts how many digits are in the second number
                if digit_number_two < 4 and digit_number_two > 0 and instruction_string[i + 5 + digit_number_one + digit_number_two] == ')': # iIf number is within allowed length and followed by a ')'
                    number_two = int(instruction_string[i + 5 + digit_number_one:i + 5 + digit_number_one + digit_number_two]) # Sets variable number_two to the second number in the mul
                    total += number_one * number_two
        elif instruction_string[i:i + 7] == 'don\'t()': # If 'don't()' is found
            do_instruction = False
    elif instruction_string[i:i + 4] == 'do()': # If 'do()' is found
        do_instruction = True

print(total)