# For an equation of n values, there are 2^(n-1) combinations of symbols.
# This allows for a binary number to represent + as 0 and * as 1, and
# use that to easily try every combination. This functions then returns
# If it's possible to solve.
def is_possible(equation):
    for i in range(2 ** (len(equation) - 2)): # len(equation) is 1 more than the number of values
        binary_value = bin(i)[2:].zfill(len(equation) - 2) # Creates a binary value of the right length
        total = equation[1]
        for j in range(len(binary_value)):
            if binary_value[j] == '0':
                total += equation[j + 2] # Adds on next value
            else:
                total *= equation[j + 2] # Multiplies by next value
        if total == equation[0]:
            return True
    return False


equations = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip().replace(':', '')
        equations.append(list(map(int, line.split(' ')))) # Creates equations list of a list of the numbers, 
                                                          #     the first being the solution

total = 0
for equation in equations:
    if is_possible(equation):
        total += equation[0]

print(total)
