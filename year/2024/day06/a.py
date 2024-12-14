import re

def main():

    grid = []
    walkgrid = []
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dir = 0
    x = 0
    y = 0
    sizex = 0


    for line in open("input.txt", "r"):
        sizex = len(line) - 1
        grid.append(line[:-1])
        walkgrid.append([False] * sizex)
        search = re.search("\^", line)
        if search:
            x = search.span()[0]
            y = len(grid) - 1
            grid[y] = grid[y].replace('^', '.')
            walkgrid[y][x] = True
    sizey = len(walkgrid)


    while(True):
        newy = y + dirs[dir%4][0]
        newx = x + dirs[dir%4][1]

        if (newx < 0 or newx >= sizex or newy < 0 or newy >= sizey):
            print("out")
            break
        
        if grid[newy][newx] == '#':
            print("turn")
            dir += 1
        else:
            y = newy
            x = newx
            walkgrid[y][x] = True

    walk = 0
    for line in walkgrid:
        print(line)
        walk += line.count(True)

    print(walk)

main()