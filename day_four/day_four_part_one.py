def count_xmas(in_string, xmas_count=0):
    if in_string == '':
        return xmas_count
    if in_string[:4] == 'XMAS':
        return count_xmas(in_string[4:], xmas_count + 1)

    return count_xmas(in_string[1:], xmas_count)

def check_right():
    total = 0
    for line in row_list:
        total += count_xmas(line)

    return total

def check_left():
    total = 0
    for line in row_list:
        total += count_xmas(line[::-1])

    return total

def check_down():
    total = 0
    for i in range(len(row_list[0])):
        string_to_check = ''
        for line in row_list:
            string_to_check += line[i]
        total += count_xmas(string_to_check)
    
    return total

def check_up():
    total = 0
    for i in range(len(row_list[0])):
        string_to_check = ''
        for line in row_list:
            string_to_check += line[i]
        total += count_xmas(string_to_check[::-1])

    return total

def check_down_right_diags():
    total = 0

    # Checks diaganols starting at the left edge
    for i in range(len(row_list) - 1, -1, -1):
        letter_pos = (0, i) # Coordinates of the current letter as (x, y)
        diaganol_string = ''
        while letter_pos[0] < len(row_list[i]) and letter_pos[1] < len(row_list): # While the current coordinates exist
            diaganol_string += row_list[letter_pos[1]][letter_pos[0]]
            letter_pos = (letter_pos[0] + 1, letter_pos[1] + 1)
        total += count_xmas(diaganol_string)

    # Checks diaganols starting at the top edge
    for i in range(1, len(row_list[0])):
        letter_pos = (i, 0) # Coordinates of the current letter as (x, y)
        diaganol_string = ''
        while letter_pos[0] < len(row_list[i]) and letter_pos[1] < len(row_list): # While the current coordinates exist
            diaganol_string += row_list[letter_pos[1]][letter_pos[0]]
            letter_pos = (letter_pos[0] + 1, letter_pos[1] + 1)
        total += count_xmas(diaganol_string)

    return total

def check_up_right_diags():
    total = 0

    # Checks diaganols starting at the left edge
    for i in range(0, len(row_list)):
        letter_pos = (0, i) # Coordinates of the current letter as (x, y)
        diaganol_string = ''
        while letter_pos[0] < len(row_list[i]) and letter_pos[1] > -1: # While the current coordinates exist
            diaganol_string += row_list[letter_pos[1]][letter_pos[0]]
            letter_pos = (letter_pos[0] + 1, letter_pos[1] - 1)
        total += count_xmas(diaganol_string)

    # Checks diaganols starting at the bottom edge
    for i in range(1, len(row_list[0])):
        letter_pos = (i, len(row_list[0]) - 1) # Coordinates of the current letter as (x, y)
        diaganol_string = ''
        while letter_pos[0] < len(row_list[i]) and letter_pos[1] > -1: # While the current coordinates exist
            diaganol_string += row_list[letter_pos[1]][letter_pos[0]]
            letter_pos = (letter_pos[0] + 1, letter_pos[1] - 1)
        total += count_xmas(diaganol_string)

    return total
        
def check_up_left_diags():
    total = 0

    # Checks diaganols starting at the left edge
    for i in range(len(row_list) - 1, -1, -1):
        letter_pos = (0, i) # Coordinates of the current letter as (x, y)
        diaganol_string = ''
        while letter_pos[0] < len(row_list[i]) and letter_pos[1] < len(row_list): # While the current coordinates exist
            diaganol_string += row_list[letter_pos[1]][letter_pos[0]]
            letter_pos = (letter_pos[0] + 1, letter_pos[1] + 1)
        total += count_xmas(diaganol_string[::-1])

    # Checks diaganols starting at the top edge
    for i in range(1, len(row_list[0])):
        letter_pos = (i, 0) # Coordinates of the current letter as (x, y)
        diaganol_string = ''
        while letter_pos[0] < len(row_list[i]) and letter_pos[1] < len(row_list): # While the current coordinates exist
            diaganol_string += row_list[letter_pos[1]][letter_pos[0]]
            letter_pos = (letter_pos[0] + 1, letter_pos[1] + 1)
        total += count_xmas(diaganol_string[::-1])

    return total

def check_down_left_diags():
    total = 0

    # Checks diaganols starting at the left edge
    for i in range(0, len(row_list)):
        letter_pos = (0, i) # Coordinates of the current letter as (x, y)
        diaganol_string = ''
        while letter_pos[0] < len(row_list[i]) and letter_pos[1] > -1: # While the current coordinates exist
            diaganol_string += row_list[letter_pos[1]][letter_pos[0]]
            letter_pos = (letter_pos[0] + 1, letter_pos[1] - 1)
        total += count_xmas(diaganol_string[::-1])

    # Checks diaganols starting at the bottom edge
    for i in range(1, len(row_list[0])):
        letter_pos = (i, len(row_list[0]) - 1) # Coordinates of the current letter as (x, y)
        diaganol_string = ''
        while letter_pos[0] < len(row_list[i]) and letter_pos[1] > -1: # While the current coordinates exist
            diaganol_string += row_list[letter_pos[1]][letter_pos[0]]
            letter_pos = (letter_pos[0] + 1, letter_pos[1] - 1)
        total += count_xmas(diaganol_string[::-1])

    return total



row_list = []
with open('input.txt', 'r') as f:
    for line in f:
        row_list.append(line.strip()) # Can address each letter with row_list[y][x]


total = 0
total += check_right()
total += check_left()
total += check_up()
total += check_down()
total += check_up_right_diags()
total += check_down_right_diags()
total += check_up_left_diags()
total += check_down_left_diags()
print (total)
# This is probably the worst solution anyone could have come up with...