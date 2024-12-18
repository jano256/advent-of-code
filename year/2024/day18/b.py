from operator import add
import copy
import sys
sys.setrecursionlimit(10000)

def main():
    global d
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    global grid
    start = [1, 1]
    end = [71, 71]
    length = 2500
    
    startgrid = [[9999999 for x in range(end[0])] for y in range(end[1])]
    for x in range(end[1]):
        startgrid[x].insert(0, '#')
        startgrid[x].append('#')
    startgrid.insert(0, ['#'] * (end[0] + 2))
    startgrid.append(['#'] * (end[0] + 2))

    ops = []
    for line in open("input.txt", "r"):
        ops.append(list(map(int, line[:-1].split(','))))

    for i in range(length):
        startgrid[ops[i][1]+1][ops[i][0]+1] = '#'

    moves = 0
    while moves < 9999999:
        grid = copy.deepcopy(startgrid)
        #print_grid(startgrid)
        move(start)
        moves = grid[end[1]][end[0]]
        print(moves)
        length += 1
        startgrid[ops[length][1]+1][ops[length][0]+1] = '#'
    print(ops[length-1])
    

def move(pos, point=1):
    for i in range(4):
        x , y = map(add, pos, d[i])
        if grid[y][x] != '#':
            if grid[y][x] > point:
                grid[y][x] = point
                move([x, y], point+1)


def print_grid(grd):
    for line in grd:
        for char in line:
            print(char, ' ', end='')
        print()

main()