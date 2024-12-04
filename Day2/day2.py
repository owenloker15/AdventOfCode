def isOk(numbers):
    ok = True
    all_increasing = True
    all_decreasing = True
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff > 0:
            all_decreasing = False
        elif diff < 0:
            all_increasing = False

        if not 1 <= abs(diff) <= 3:
            ok = False
            break
    
    return ok and (all_increasing or all_decreasing)

def checkAllSolutions(numbers):
    if isOk(numbers):
        return True
    
    for i in range(len(numbers)):
        copy = numbers.copy()
        copy.pop(i)
        if isOk(copy):
            return True
        
    return False

lines = []

with open("day2input.txt", "r") as file:
    lines = file.readlines()

clean_lines = [line.strip() for line in lines]

count = 0

for line in clean_lines:
    numbers = [int(num) for num in line.split()]

    if checkAllSolutions(numbers):
        count += 1


print(count)
