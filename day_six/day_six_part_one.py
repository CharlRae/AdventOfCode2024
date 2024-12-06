map_list = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        map_list.append(list(line))


position_history = []
# Finds current position of the guard
for y in range(len(map_list)):
    for x in range(len(map_list[y])):
        symbol = map_list[y][x]
        if symbol in ['^', '>', 'v', '<']:
            current_position = {'x':x, 'y':y}
            break
    else:
        continue
    break


while current_position['x'] > -1 and current_position['x'] < len(map_list[0]) and current_position['y'] > -1 and current_position['y'] < len(map_list): # While guard is in the lab
    if (current_position['x'], current_position['y']) not in position_history: # Adds position to history if it isn't already
        position_history.append((current_position['x'], current_position['y']))

    # Handles movement and rotations
    match symbol:
        case '^':
            if current_position['y'] > 0: # If not on top edge
                if map_list[current_position['y'] - 1][current_position['x']] == '#': # If there is an obstacle in front
                    symbol = '>' # Rotate 90 degrees
                else:
                    current_position['y'] -= 1 # Move forward
            else:
                current_position['y'] -= 1 # Move forward

        case '>':
            if current_position['x'] < len(map_list[current_position['y']]) - 1: # If not on right edge
                if map_list[current_position['y']][current_position['x'] + 1] == '#': # If there is an obstacle in front
                    symbol = 'v' # Rotate 90 degrees
                else:
                    current_position['x'] += 1 # Move forward
            else:
                current_position['x'] += 1 # Move forward
        
        case 'v':
            if current_position['y'] < len(map_list) - 1: # If not on bottom edge
                if map_list[current_position['y'] + 1][current_position['x']] == '#': # If there is an obstacle in front
                    symbol = '<' # Rotate 90 degrees
                else:
                    current_position['y'] += 1 # Move forward
            else:
                current_position['y'] += 1 # Move forward

        case '<':
            if current_position['x'] > 0: # If not on left edge
                if map_list[current_position['y']][current_position['x'] - 1] == '#': # If there is an obstacle in front
                    symbol = '^' # Rotate 90 degrees
                else:
                    current_position['x'] -= 1 # Move forward
            else:
                current_position['x'] -= 1 # Move forward

print(len(position_history))