import string, itertools

def main():
    grid = []
    sizex = 0
    sizey = 0

    for line in open("input.txt", "r"):
        sizex = len(line) - 1
        sizey += 1
        grid.append('.' + line[:-1] + '.')
    grid.insert(0, (sizex + 2) * '.')
    grid.append((sizex + 2) * '.')
    
    trailheads = []
    for y in range(1, sizey + 1):
        for x in range(1, sizex + 1):
            if grid[y][x] == '0':
                trailheads.append([x, y])

    sum_a = 0
    sum_b = 0
    for trailhead in trailheads:
        global hits
        hits = []
        move(trailhead[0], trailhead[1], 0, grid)
        sum_a += len(set(hits))
        sum_b += len(hits)
    print("PartA:", sum_a, "  PartB:", sum_b)


def move(x, y, num, grid):
    num = str(int(num) + 1)
    if num == "10":
        hits.append(str(x) + ',' + str(y))
    if grid[y][x+1] == num:
        move(x+1, y, num, grid)
    if grid[y][x-1] == num:
        move(x-1, y, num, grid)
    if grid[y+1][x] == num:
        move(x, y+1, num, grid)
    if grid[y-1][x] == num:
        move(x, y-1, num, grid)

main()