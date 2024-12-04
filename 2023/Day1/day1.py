import re

words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open("day1input.txt", "r") as file:
    lines = file.readlines()

sum = 0
for line in lines:
    nums = re.findall(r'(\d){1}|(one|two|three|four|five|six|seven|eight|nine)' , line)
    all = [value for num in nums for value in num if value != '']
    
    first = all[0]
    last = all[-1]
    
    if first in words:
        first = words[first]
        
    if last in words:
        last = words[last]
    
    ans = int(first + last)
    sum += ans

print(sum)