x, y = 0, 1
def main():
    dir = {'^': [0, -1], 'v': [0, 1], '<': [-1, 0], '>': [1, 0]}
    pos = [0, 0]
    grid = []
    grid_finish = False
    moves = []

    for line in open("input.txt", "r"):
        if line == '\n':
                grid_finish = True
                continue
        if not grid_finish:
            grid.append([])
            for char in line[:-1]:
                grid[-1].append(char)    
        else:
            moves += line[:-1]

    for line in grid:
        if line.count('@'):
            pos[x], pos[y] = line.index('@'), grid.index(line)
            grid[pos[y]][pos[x]] = '.'

    for m in moves:
        target_x, target_y = pos[x] + dir[m][x], pos[y] + dir[m][y]
        target = grid[target_y][target_x]
        
        match target:
            case '#':
                continue
            case '.':
                pos[x], pos[y] = target_x, target_y
            case 'O':
                move_x, move_y = target_x, target_y
                while True:
                    move_x, move_y = move_x + dir[m][x], move_y + dir[m][y]
                    match grid[move_y][move_x]:
                        case '.':
                            grid[target_y][target_x], grid[move_y][move_x] = grid[move_y][move_x], grid[target_y][target_x]
                            pos[x], pos[y] = target_x, target_y
                            break
                        case '#':
                            break

    sum = 0
    for line in range(len(grid)):
        for point in range(len(grid[0])):
            if grid[line][point] == 'O':
                sum += 100 * line + point
    print(sum)

main()