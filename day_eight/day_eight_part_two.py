def find_antinodes(position_1, position_2):
    difference_x = position_1[0] - position_2[0]
    difference_y = position_1[1] - position_2[1]
    antinode_list = []
    
    x = position_1[0] # Start at the first position
    y = position_1[1]
    while 0 <= x < len(map_list) and 0 <= y < len(map_list): # While the coordinates exist
        coordinate = (x, y)
        if coordinate not in antinode_list: # Add new antinode if it's not already in there
            antinode_list.append(coordinate)
        x += difference_x # Increase coordinates by the distance between the antennas
        y += difference_y

    x = position_1[0] - difference_x # This time, start 1 step behind the antenna, as antenna has already been counted
    y = position_1[1] - difference_y
    while 0 <= x < len(map_list) and 0 <= y < len(map_list):
        coordinate = (x, y)
        if coordinate not in antinode_list:
            antinode_list.append(coordinate)
        x -= difference_x # Decrease coordinates by the distance between the antennas
        y -= difference_y
        

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