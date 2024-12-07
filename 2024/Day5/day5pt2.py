from collections import defaultdict

def follows_rules(update, rules):
    indices = {}
    for i, num in enumerate(update):
        indices[num] = i
        
    for first, second in rules:
        if first in indices and second in indices and not indices[first] < indices[second]:
            return False, 0
    
    return True, update[len(update) // 2]

def sort_correctly(update, rules):
    while True:
        is_sorted = True
        for i in range(len(update) - 1):
            if (update[i + 1], update[i]) in rules:
                is_sorted = False
                update[i], update[i + 1] = update[i + 1], update[i]
        
        if is_sorted:
            return update

with open("day5input.txt", "r") as file:
    raw_rules, raw_updates = file.read().strip().split("\n\n")
    rules = []
    for line in raw_rules.split('\n'):
        first, second = line.split('|')
        rules.append((int(first), int(second)))
    
    updates = [list(map(int, line.split(','))) for line in raw_updates.split('\n')]

sum = 0

for update in updates:
    follows, middle = follows_rules(update, rules)
    if follows:
        continue
    
    seq = sort_correctly(update, rules)
    sum += seq[len(seq) // 2]
        
print(sum)