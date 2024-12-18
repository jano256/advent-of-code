from operator import add
import sys
sys.setrecursionlimit(10000)

def main():
    global d
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    global grid
    start = [1, 1]
    end = [71, 71]
    len = 1024
    
    grid = [[9999999 for x in range(end[0])] for y in range(end[1])]
    for x in range(end[1]):
        grid[x].insert(0, '#')
        grid[x].append('#')
    grid.insert(0, ['#'] * (end[0] + 2))
    grid.append(['#'] * (end[0] + 2))

    i = 0
    for line in open("input.txt", "r"):
        if i == len: break
        x, y = map(int, line[:-1].split(','))
        grid[y+1][x+1] = '#'
        i += 1

    move(start)
    print(grid[end[1]][end[0]])
    

def move(pos, point=1):
    for i in range(4):
        x , y = map(add, pos, d[i])
        if grid[y][x] != '#':
            if grid[y][x] > point:
                grid[y][x] = point
                move([x, y], point+1)


main()