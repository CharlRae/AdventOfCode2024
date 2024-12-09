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
while front_pointer < rear_pointer:
    if file_system_merged[rear_pointer] == '.': # Moves rear pointer until it's a file
        rear_pointer -= 1
    elif file_system_merged[front_pointer] != '.': # Moves front point until it's not a file
        front_pointer += 1
    else: # When rear is a file and front is free, swap them
        file_system_merged[front_pointer], file_system_merged[rear_pointer] = file_system_merged[rear_pointer], file_system_merged[front_pointer]

# Calculates checksum
total = 0
for i in range(len(file_system_merged)):
    if file_system_merged[i] != '.':
        total += int(file_system_merged[i]) * i
print(total)