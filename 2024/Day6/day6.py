import copy

orientation = {"^": (-1 , 0), ">": (0, 1), "V": (1, 0), "<": (0, -1)}
rotation = list(orientation.keys())

def loop(grid, curr_pos, found_tiles):
    while True:
        if not curr_pos in found_tiles:
            found_tiles.add(curr_pos)
        curr_tile = grid[curr_pos[0]][curr_pos[1]]
        dir = orientation[curr_tile]
        
        next_pos = curr_pos[0] + dir[0], curr_pos[1] + dir[1]
        
        if not 0 <= next_pos[0] < len(grid) or not 0 <= next_pos[0] < len(grid[0]):
            return False
        
        next_tile = grid[next_pos[0]][next_pos[1]]
        if next_tile == "#":
            rot_idx = rotation.index(curr_tile)
            grid[curr_pos[0]][curr_pos[1]] = rotation[(rot_idx + 1) % len(rotation)]
            next_pos = curr_pos
        else:
            temp = grid[curr_pos[0]][curr_pos[1]]
            grid[curr_pos[0]][curr_pos[1]] = grid[next_pos[0]][next_pos[1]]
            grid[next_pos[0]][next_pos[1]] = temp
        curr_pos = next_pos

with open("day6input.txt") as file:
    lines = file.read().strip().split("\n")
    
grid = [list(line) for line in lines]

start_pos = None
for i, row in enumerate(grid):
        if "^" in row:
            start_pos = i, row.index("^")

found_tiles = set()

loop(grid, start_pos, found_tiles)

print(len(found_tiles))