import re

with open("day3input.txt", "r") as file:
    string = file.read()

found = re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(do(?:n\'t)*\(\))' , string)

sum = 0
enabled = True
for pair, enableStr in found:
    if not enableStr == '':
        if enableStr == 'do()':
            enabled = True
        elif enableStr == 'don\'t()':
            enabled = False
        continue
        
    if enabled:
        numsFound = re.findall(r'\d{1,3}', pair)
        if not len(numsFound) == 2:
            continue

        sum += int(numsFound[0]) * int(numsFound[1])

print(sum)
