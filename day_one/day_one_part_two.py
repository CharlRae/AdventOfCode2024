# Calculates the similarity of the two lists
def score_similarity(list_one, list_two):
    total = 0
    known_repeats = {}

    for i in range(len(list_one)):
        if list_one[i] not in known_repeats: # If this number has not been seen before, count it and add it to the dictionary
            known_repeats[list_one[i]] = list_two.count(list_one[i])
        total += list_one[i] * known_repeats[list_one[i]] # Add the number * how many times it appears in list 2 to the total

    return total

# Creates the two lists from the file, sorts them, and returns them both in a tuple
def setup_lists(file_name):
    list_one = []
    list_two = []

    with open(file_name, 'r') as f: Adds a new element per line of the fil
        for line in f:
            line_list = line.split()
            list_one.append(line_list[0])
            list_two.append(line_list[1])

    list_one.sort()
    list_two.sort()
    list_one = list(map(int, list_one)) # Casts each element in the list to int
    list_two = list(map(int, list_two))

    return (list_one, list_two)



list_tuple = setup_lists('Y:\w2k\Desktop\Advent of Code\day_one\input.txt')
list_one = list_tuple[0] # Take the list from the tuple
list_two = list_tuple[1]
print(score_similarity(list_one, list_two))
