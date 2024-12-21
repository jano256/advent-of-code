from operator import add
import sys
import copy

sys.setrecursionlimit(10000)

def main():
    global d
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    grid = []
    start = [0, 0]
    end = [0, 0]
    for line in open("input.txt", "r"):
        grid.append([])
        for char in line[:-1]:
            if char == 'S': start = [len(grid[-1]), len(grid)-1]
            if char == 'E': end   = [len(grid[-1]), len(grid)-1]
            if char == '#': grid[-1].append('#')
            else: grid[-1].append(99999999999)
    
    global testgrid
    testgrid = copy.deepcopy(grid)
    move(start)
    base = testgrid[end[1]][end[0]]

    cheats = 0
    for x in range(1, len(grid[0]) -1):
        for y in range(1, len(grid) -1):
            if grid[y][x] == '#':
                testgrid = copy.deepcopy(grid)
                testgrid[y][x] = 99999999999
                move(start)
                new = testgrid[end[1]][end[0]]
                save = base - new
                if save >= 100:
                    cheats += 1
                    print(save)
    
    print("cheats:", cheats)

def move(pos, point=1):
    for i in range(4):
        x , y = map(add, pos, d[i])
        if testgrid[y][x] != '#':
            if testgrid[y][x] > point:
                testgrid[y][x] = point
                move([x, y], point+1)

main()