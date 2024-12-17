from operator import add
import sys
sys.setrecursionlimit(10000)

def main():
    global d
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    global grid
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

    
    move(start)
    print(grid[end[1]][end[0]])

def move(pos, dir=0, point=0):
    if grid[pos[1]][pos[0]] < point:
        return
    grid[pos[1]][pos[0]] = point
    for i in [0, 1, -1]:
        x , y = map(add, pos, d[(dir + i)%4])
        if grid[y][x] != '#':
            move([x, y], dir+i, point+1+abs(i)*1000)


def print_grid(grid):
    for line in grid:
        print(line)

main()