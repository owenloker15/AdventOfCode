def search_letter(puzzle, row, col):
    letter = puzzle[row][col]
    
    if letter != 'A':
        return False
    if not 1 <= row < len(puzzle[0]) - 1 or not 1 <= col < len(puzzle) - 1:
        return False
    
    left_diag = (puzzle[row - 1][col + 1], puzzle[row + 1][col - 1])
    right_diag = (puzzle[row - 1][col - 1], puzzle[row + 1][col + 1])
    
    if not left_diag in [('M', 'S'), ('S', 'M')] or not right_diag in [('M', 'S'), ('S', 'M')]:
        return False
        
    return True

def solve(puzzle):
    count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if search_letter(puzzle, i, j): 
                count += 1             
    
    return count

def main():
    puzzle = []
    with open("day4input.txt", "r") as file:
        for line in file:
            clean_line = line.strip()
            row = []
            for char in clean_line:
                row.append(char)
            puzzle.append(row)

    print(solve(puzzle))
    
if __name__ == "__main__":
    main()