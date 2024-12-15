import re
x, y = 0, 1

def main():
    dir = {'^': [0, -1], 'v': [0, 1], '<': [-1, 0], '>': [1, 0]}
    pos = [0, 0]
    grid = []
    for line in open("test.txt", "r"):
        grid.append([])
        for char in line[:-1]:
            grid[-1].append(char)
    moves = grid[-1].copy()
    grid.pop(-1)
    grid.pop(-1)

    for line in grid:
        if line.count('@'):
            pos[x] = line.index('@')
            pos[y] = grid.index(line)
            grid[pos[y]][pos[x]] = '.'

    for m in moves:
        target_x, target_y = pos[x] + dir[m][x], pos[y] + dir[m][y]
        print_grid(grid, pos)
        print("move", dir[m])
        print("pos", pos)
        print("target", target_x, target_y)
        target = grid[target_y][target_x]
        input("press enter")
        
        if target == '#':
            continue

        if target == 'O':
            if not try_push():
                continue

        pos[x] = target_x
        pos[y] = target_y
        
def try_push():
    return True

def print_grid(grid, pos):
    for line in range(len(grid[0])):
        for point in range(len(grid)):
            if line == pos[y] and point == pos[x]:
                print('@', end='')
            else:
                print(grid[line][point], end='')
        print()
    
        
main()