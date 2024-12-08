def find_antinodes(position_1, position_2):
    difference_x = position_1[0] - position_2[0]
    difference_y = position_1[1] - position_2[1]
    antinode_list = []

    # Adds an antinode the same distance, but opposite direction from the first antenna to the second
    if position_1[0] + difference_x == position_2[0] and position_1[1] + difference_y == position_2[1]:
        antinode_list.append((position_1[0] - difference_x, position_1[1] - difference_y))
    else:
        antinode_list.append((position_1[0] + difference_x, position_1[1] + difference_y))

    # Adds an antinode the same distance, but opposite direction from the second tower to the first
    if position_2[0] + difference_x == position_1[0] and position_2[1] + difference_y == position_1[1]:
        antinode_list.append((position_2[0] - difference_x, position_2[1] - difference_y))
    else:
        antinode_list.append((position_2[0] + difference_x, position_2[1] + difference_y))

    # Removes antinodes which are outside the map
    for i in range(len(antinode_list) - 1, -1, -1):
        if not (0 <= antinode_list[i][0] < len(map_list[0]) and 0 <= antinode_list[i][1] < len(map_list)):
            del antinode_list[i]

    return antinode_list



with open('input.txt', 'r') as f:
    map_list = f.read().split() # Stores the map as a list of strings, can be addresses with map_list[y][x]

found_frequencies = set()
antinodes = []
antenna_coordinates = []
for y in range(len(map_list)): # Iterate over every position
    for x in range(len(map_list[y])):
        symbol = map_list[y][x]
        if symbol != '.': # If the current symbol is an antenna
            if symbol not in found_frequencies: # If not already seen this frequency
                found_frequencies.add(symbol) # Registers this as a found frequency
            else:
                for coordinates in antenna_coordinates: # Iterates over every known antenna's coordinates
                    if coordinates['frequency'] == symbol: # If the antenna is on the same frequency
                        new_antinodes = find_antinodes((x, y), (coordinates['x'], coordinates['y'])) # Adds the new antinodes
                        for new_antinode in new_antinodes:
                            if new_antinode not in antinodes:
                                antinodes.append(new_antinode) # Adds any antinotes which have not already been discovered
            antenna_coordinates.append({'frequency':symbol, 'x':x, 'y':y}) # Adds new symbol and coordinates

print(len(antinodes))