lines = []
list1 = []
list2 = []


with open("day1input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    numbers = line.split()
    list1.append(int(numbers[0]))
    list2.append(int(numbers[1]))

# part 1

list1 = sorted(list1)
list2 = sorted(list2)

sum = 0

for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)

# part 2
simScore = 0

intersection = [value for value in list1 if value in list2]
for value in intersection:
    simScore += list2.count(value) * value

print(simScore)
