# Finds all rules relevant to can update
def find_rules(update):
    matching_rules = []
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            matching_rules.append(rule)

    return matching_rules

# Checks if an update meets a rule
def meets_rule(rule, update):
    for page in update:
        if page == rule[0]: # If first page found first
            return True
        if page == rule[1]: # If second page found first
            return False
        
    return True

# Checks if an update meets all the rules
def meets_all_rules(update, matching_rules):
    for rule in matching_rules:
        if not meets_rule(rule, update):
            return False
        
    return True

# Swaps pairs of page numbers in the incorrect order until the update meets all rules
def fix_ordering(update, matching_rules):
    new_update = update.copy()
    while not meets_all_rules(new_update, matching_rules):
        for rule in matching_rules:
            before_index = new_update.index(rule[0]) # Sets index of the number that's supposed to be before
            after_index = new_update.index(rule[1])
            if before_index > after_index:
                # Swaps the page numbers around
                temp = new_update[before_index]
                new_update[before_index] = new_update[after_index] 
                new_update[after_index] = temp

    return new_update



# Sets up rules and updates lists
updates = []
rules = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if '|' in line:
            rules.append(line.split('|'))
        elif line != '':
            updates.append(line.split(','))

# Creates a list of all updates that don't meet the rules
invalid_updates = []
for update in updates:
    matching_rules = find_rules(update)
    if not meets_all_rules(update, matching_rules):
        invalid_updates.append(update)

# Fixes the broken updates
fixed_updates = []
for update in invalid_updates:
    matching_rules = find_rules(update)
    fixed_updates.append(fix_ordering(update, matching_rules))

# Sums the middle item in each fixed update
total = 0
for update in fixed_updates:
    middle_index = len(update) // 2
    total += int(update[middle_index])
print(total)