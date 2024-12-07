def valid_pages(order, pages):
    # if second page is found in the order before the first page, no good
    for i in range(len(pages) - 1):
        first_page = pages[i]
        second_page = pages[i + 1]
        
        if not order.index(first_page) < order.index(second_page):
            return False
    return True

with open("day5input.txt", "r") as file:
    lines = file.readlines()

idx = 0
line = lines[idx]
order = []
while line != '\n':
    line = line.strip()
    first, second = line.split('|')
    
    # Add first to beginning of the order
    if first not in order:
        order.insert(0, first)
    
    # Add second to end of the order
    if second not in order:
        order.append(second)
    
    # Make sure first is in front of second, if its not, put it in front of second
    first_index = order.index(first)
    second_index = order.index(second)
    if first_index > second_index:
        order.pop(first_index)
        order.insert(second_index, first)
    
    idx += 1
    line = lines[idx]
    
# Convert to list of ints
order = [int(item) for item in order]

sum = 0

print(order)

# iterate through each page that needs to be check to add to update
for line in lines[idx + 1:len(lines)]:
    line = line.strip()
    pages = line.split(',')
    pages = [int(page) for page in pages]
    
    # if page is valid, add the middle one to the sum
    if valid_pages(order, pages):
        middle_page_in_list_idx = int(len(pages) / 2)
        num = pages[middle_page_in_list_idx]
        sum += num
        
    
print(sum)