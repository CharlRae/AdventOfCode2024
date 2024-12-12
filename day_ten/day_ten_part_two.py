# Creates map_list, a 2D array representing the map
map_list = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = list(map(int, list(line))) # Converts line to a list of integers
        map_list.append(line)

# Finds trails from a start coordinate of (x, y)
def find_trails(this_trail, height=0):
    if height == 9:
        trail_list.append(this_trail)
        return None
    # Check above
    if this_trail[-1][1] - 1 >= 0 and map_list[this_trail[-1][1] - 1][this_trail[-1][0]] == height + 1:
        find_trails(this_trail + [(this_trail[-1][0], this_trail[-1][1] - 1)], height + 1)
    # Check below
    if this_trail[-1][1] + 1 < len(map_list) and map_list[this_trail[-1][1] + 1][this_trail[-1][0]] == height + 1:
        find_trails(this_trail + [(this_trail[-1][0], this_trail[-1][1] + 1)], height + 1)
    # Check left
    if this_trail[-1][0] - 1 >= 0 and map_list[this_trail[-1][1]][this_trail[-1][0] - 1] == height + 1:
        find_trails(this_trail + [(this_trail[-1][0] - 1, this_trail[-1][1])], height + 1)
    # Check right
    if this_trail[-1][0] + 1 < len(map_list) and map_list[this_trail[-1][1]][this_trail[-1][0] + 1] == height + 1:
        find_trails(this_trail + [(this_trail[-1][0] + 1, this_trail[-1][1])], height + 1)



total = 0

for y in range(len(map_list)):
    for x in range(len(map_list[y])):
        coordinate = (x, y)
        if map_list[coordinate[1]][coordinate[0]] == 0: # If coordinate is a 0
            # Resets variables
            trail_list = []
            rating = 0
            find_trails([coordinate])
            for trail in trail_list: # Counts each trail starting at that position
                    rating += 1
            total += rating
            
print(total)