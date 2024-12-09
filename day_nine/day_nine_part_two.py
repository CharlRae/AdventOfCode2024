with open('input.txt', 'r') as f:
    data = f.read().strip()

file_system = []

for i in range(0, len(data)): # Iterates every other index
    if int(data[i]) > 0 and i % 2 == 0:
        file_system.append([str(i // 2)] * int(data[i])) # Adds data
    elif int(data[i]) > 0 and i % 2 == 1:
        file_system.append(['.'] * int(data[i])) # Adds free space

# Merges file groups together
file_system_merged = []
for i in file_system:
    file_system_merged += i

# Moves files into first free space
front_pointer = 0
rear_pointer = len(file_system_merged) - 1
space_size = 0
file_number = None
file_start = len(file_system_merged) - 1

while rear_pointer > 0:
    # Gives up searching for a space if it can't find any to the left
    if front_pointer > file_start:
        front_pointer = 0
        file_number = None

    # Finds the length and number of the next file
    if file_number == None:
        # Finds the next file, it's number and size
        file_number = file_system_merged[rear_pointer]
        while file_number == None or file_number == '.':
            rear_pointer -= 1
            file_number = file_system_merged[rear_pointer]
        file_start = rear_pointer
        while file_system_merged[rear_pointer] == file_number:
            rear_pointer -= 1
        file_size = file_start - rear_pointer

    # Moves file into space if it fits
    if space_size == file_size:
        file_system_merged = file_system_merged[:space_start] + file_system_merged[file_start - file_size + 1:file_start + 1] + file_system_merged[space_start + space_size:file_start - file_size + 1] + file_system_merged[space_start:space_start + space_size] + file_system_merged[file_start + 1:]
        file_number = None
        front_pointer = 0

    # Updates the space size/start index
    if file_system_merged[front_pointer] == '.':
        if space_size == 0:
            space_start = front_pointer # Saves the index of the start of the space
        space_size += 1
    else:
        space_size = 0
    front_pointer += 1

    
    
    

# Calculates checksum
total = 0
for i in range(len(file_system_merged)):
    if file_system_merged[i] != '.':
        total += int(file_system_merged[i]) * i
print(total)