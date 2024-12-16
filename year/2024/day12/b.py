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
                global area
                area = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
                move(x, y, grid[y][x], grid)

                fence = 0
                for i in [-1, 1]:
                    for yy in range(1, len(grid)-1):
                        begin = False
                        for xx in range(1, len(grid[0])-1):
                            if not area[yy+i][xx] and area[yy][xx]:
                                if begin == False:
                                    begin = True
                                    fence += 1
                            else:
                                if begin:
                                    begin = False

                for i in [-1, 1]:
                    for xx in range(1, len(grid[0])-1):
                        begin = False
                        for yy in range(1, len(grid)-1):
                            if not area[yy][xx+i] and area[yy][xx]:
                                if begin == False:
                                    begin = True
                                    fence += 1
                            else:
                                if begin:
                                    begin = False

                sum += fence * hits                  
                            
    print(sum)


def move(x, y, type, grid):
    global area
    global hits
    hits += 1
    area[y][x] = True
    grid[y][x] = type.lower()

    if grid[y][x+1] == type: move(x+1, y, type, grid)
    if grid[y][x-1] == type: move(x-1, y, type, grid)
    if grid[y+1][x] == type: move(x, y+1, type, grid)
    if grid[y-1][x] == type: move(x, y-1, type, grid)

main()