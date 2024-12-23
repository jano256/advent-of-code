import string, itertools

def main():

    grid = []
    sizex = 0
    sizey = 0

    for line in open("input.txt", "r"):
        sizex = len(line) - 1
        sizey += 1
        grid.append(line[:-1])
        
    antinodes = [[False for x in range(sizex)] for y in range(sizey)]

    alphanum_list = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    antenna_list = []
    for i in alphanum_list:
        antenna_list.append([])

    for x in range(sizex):
        for y in range(sizey):
            if grid[y][x] != '.':
                antenna_list[alphanum_list.index(grid[y][x])].append([x, y])

    for char in alphanum_list:
        antennas = antenna_list[alphanum_list.index(char)]
        for combos in itertools.combinations(antennas, 2):
            x1 = 2 * combos[0][0] - combos[1][0]
            y1 = 2 * combos[0][1] - combos[1][1]
            x2 = 2 * combos[1][0] - combos[0][0]
            y2 = 2 * combos[1][1] - combos[0][1]
            set_antinode(antinodes, x1, y1, sizex, sizey)
            set_antinode(antinodes, x2, y2, sizex, sizey)

    antinode_count = 0
    for line in antinodes:
        antinode_count += line.count(True)
    print(antinode_count)


def set_antinode(antinodes, x, y, sizex, sizey):
    if (x < 0 or x >= sizex or y < 0 or y >= sizey):
        return False
    antinodes[y][x] = True
    return True

main()