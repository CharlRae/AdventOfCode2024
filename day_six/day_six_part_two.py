# Runs a simulation with the new obstruction in place, and returns if the guard ended up in a loop
def creates_loop(obstruction_position):
    original_symbol = map_list[obstruction_position['y']][obstruction_position['x']] # Saves the original symbol (this was much faster than making a deep copy of the list each time)
    if map_list[obstruction_position['y']][obstruction_position['x']] not in ['^', '>', 'v', '<', '#']: # Adds obstruction if necessary
        map_list[obstruction_position['y']][obstruction_position['x']] = '#'
    else:
        return False # Skips simulation if nothing has changed

    position_history = set() # Using a set for this was much more efficient than a list
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

    in_loop = False
    while current_position['x'] > -1 and current_position['x'] < len(map_list[0]) and current_position['y'] > -1 and current_position['y'] < len(map_list) and not in_loop: # While guard is in the lab

        current_state = (current_position['x'], current_position['y'], symbol)
        if current_state in position_history: # Checks if this exact scenario has ocurred before, if it has, it's a loop
            in_loop = True
        else:
            position_history.add(current_state) # Updates position history

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
    map_list[obstruction_position['y']][obstruction_position['x']] = original_symbol # Replaces the original symbol
    return in_loop


map_list = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        map_list.append(list(line))

total = 0
for y in range(len(map_list)):
    for x in range(len(map_list[y])):
        if creates_loop({'x':x, 'y':y}): # If the new obstructions creates a loop
            total += 1
print(total)