TARGET_WORD = "XMAS"

def create_grid():
    grid = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                grid.append((i, j))
    return grid

def search_letter(puzzle, row, col, dir):
    x_dir, y_dir = dir
    for i, char in enumerate(TARGET_WORD):
        current_x = col + i * x_dir
        current_y = row + i * y_dir
        if not 0 <= current_x < len(puzzle[0]) or not 0 <= current_y < len(puzzle):
            return False
        if(puzzle[current_x][current_y] != char):
            return False
        
    return True

def solve(puzzle, grid):
    count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            for dir in grid:
                if search_letter(puzzle, i, j, dir):
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

    grid = create_grid()
    print(solve(puzzle, grid))
    
if __name__ == "__main__":
    main()