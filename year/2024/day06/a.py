import re

def main():

    grid = []
    x = 0
    y = 0
    sizex = 0
    sizey = 0

    for line in open("input.txt", "r"):
        sizex = len(line) - 1
        sizey += 1
        grid.append(line[:-1])
        
        search = re.search("\^", line)
        if search:
            x = search.span()[0]
            y = len(grid) - 1
            grid[y] = grid[y].replace('^', '.')

    loops = 0
    for xx in range(sizex):
        for yy in range(sizey):
            if xx == x and yy == y:
                continue
            copygrid = [row[:] for row in grid]
            index = xx
            copygrid[yy] = copygrid[yy][:index] + '#' + copygrid[yy][index + 1:]



            if test(y, x, sizey, sizex, copygrid):
                loops += 1
    print(loops)



def test(starty, startx, sizey, sizex, grid):
    y = starty
    x = startx
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dir = 0
    walkgrid = []
    for i in range(sizey):
        walkgrid.append([0] * sizex)
    walkgrid[y][x] = 1
    while(True):
        newy = y + dirs[dir%4][0]
        newx = x + dirs[dir%4][1]

        if (newx < 0 or newx >= sizex or newy < 0 or newy >= sizey):
            #print("out")
            break
        
        if grid[newy][newx] == '#':
            dir += 1
        else:
            y = newy
            x = newx
            walkgrid[y][x] += 1
            if  walkgrid[y][x] > 4:
                print("same")
                return True


    walk = 0
    for line in walkgrid:
        #print(line)
        walk += line.count(0)

    #print(walk)
    return False

main()