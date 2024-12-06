def valid_pages(order, pages):
    for i in range(1, len(pages)):
        prev_page = pages[i - 1]
        curr_page = pages[i]
        
        before_pages = order[curr_page]
        
        if not prev_page in before_pages:
            return False
    return True

def correct_invalid_pages(order, pages):
    updated = False
    print(pages)
    for i in range(1, len(pages)):
        prev_page = pages[i - 1]
        curr_page = pages[i]
        before_pages = []
        
        if curr_page in order:
            before_pages = order[curr_page]
        
        if not prev_page in before_pages:
            pages[i-1], pages[i] = pages[i], pages[i-1]
            updated = True
            
    print(pages)
            
    if updated:
        if valid_pages(order, pages):
            return pages
    return []

with open("day5input.txt", "r") as file:
    lines = file.readlines()

idx = 0
line = lines[idx]
order = {}
while line != '\n':
    line = line.strip()
    first, second = line.split('|')
    
    if not second in order:
        order[second] = [first]
    else:
        if not first in order[second]:
            order[second].append(first)
    
    idx += 1
    line = lines[idx]

sum = 0

# iterate through each page that needs to be check to add to update
for line in lines[idx + 1:len(lines)]:
    line = line.strip()
    pages = line.split(',')
    
    # PT 1
    # if page is valid, add the middle one to the sum
    # if valid_pages(order, pages):
    
    # PT 2
    pages = correct_invalid_pages(order, pages)
    if pages:
        middle_page_in_list_idx = int(len(pages) / 2)
        num = int(pages[middle_page_in_list_idx])
        sum += num
        
    
print(sum)

97,75,47,61,53