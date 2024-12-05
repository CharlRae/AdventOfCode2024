row_list = []
with open('input.txt', 'r') as f:
    for line in f:
        row_list.append(line.strip()) # Can address each letter with row_list[y][x]

total = 0
for y in range(1, len(row_list)):
    for x in range(1, len(row_list[y])):
    # For each letter in the file
        try:
            if row_list[y][x] == 'A':
                string_one = row_list[y-1][x-1] + row_list[y+1][x+1]
                string_two = row_list[y+1][x-1] + row_list[y-1][x+1]
                if (string_one == 'MS' or  string_one == 'SM') and (string_two == 'MS' or string_two == 'SM'):
                    total += 1
        except:
            pass

print(total)
