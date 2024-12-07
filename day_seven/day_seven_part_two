# Converts a decimal number to base 3
def ternary(n):
    if n == 0:
        return ''
    return ternary(n // 3) + str(n % 3)

# For an equation of n values, there are 3^(n-1) combinations of symbols.
# This allows for a base 3 number to represent + as 0, * as 1, and 2 as || and
# use that to easily try every combination. This functions then returns
# If it's possible to solve.
def is_possible(equation):
    for i in range(3 ** (len(equation) - 2)): # len(equation) is 1 more than the number of values
        ternary_value = ternary(i).zfill(len(equation) - 2) # Creates a tenary value of the right length
        total = equation[1]
        for j in range(len(ternary_value)):
            if ternary_value[j] == '0':
                total += equation[j + 2] # Adds on next value
            elif ternary_value[j] == '1':
                total *= equation[j + 2] # Multiplies by next value
            else:
                total = int(str(total) + str(equation[j + 2]))
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
