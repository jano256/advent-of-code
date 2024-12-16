import string, itertools

def main():
    grid = []
    for line in open("input.txt", "r"):
        grid.append(['.', '.'])
        for char in line[:-1]:
            grid[-1].insert(-1, char)
    grid.insert(0, (len(grid[0])) * ['.'])
    grid.append((len(grid[0])) * ['.'])
    
    sum = 0
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            if grid[y][x].isupper():
                global hits
                hits = 0
                sum += move(x, y, grid[y][x], grid) * hits
    print(sum)


def move(x, y, type, grid):
    fence = 4
    global hits
    hits += 1
    grid[y][x] = type.lower()

    if grid[y][x+1].upper() == type: fence -= 1
    if grid[y][x-1].upper() == type: fence -= 1
    if grid[y+1][x].upper() == type: fence -= 1
    if grid[y-1][x].upper() == type: fence -= 1

    if grid[y][x+1] == type: fence += move(x+1, y, type, grid)
    if grid[y][x-1] == type: fence += move(x-1, y, type, grid)
    if grid[y+1][x] == type: fence += move(x, y+1, type, grid)
    if grid[y-1][x] == type: fence += move(x, y-1, type, grid)

    return fence    

main()