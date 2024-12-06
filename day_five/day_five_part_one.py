

def find_rules(update):
    matching_rules = []
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            matching_rules.append(rule)

    return matching_rules


def meets_rule(rule, update):
    for page in update:
        if page == rule[0]: # If first page found first
            return True
        if page == rule[1]: # If second page found first
            return False
    return True



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

valid_updates = []
for update in updates:
    matching_rules = find_rules(update)
    meets_rules = True
    for rule in matching_rules: # Checks if update follows all the rules
        if not meets_rule(rule, update):
            meets_rules = False
    if meets_rules:
        valid_updates.append(update)

total = 0
for update in valid_updates:
    middle_index = len(update) // 2
    total += int(update[middle_index])

print(total)