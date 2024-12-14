def main():
    robots = []
    size = [101, 103]

    for line in open("input.txt", "r"):
        pos, vel = line.split()
        pos = list(map(int, pos[2:].split(',')))
        vel = list(map(int, vel[2:].split(',')))
        robots.append({"pos": pos, "vel": vel})
    
    for i in range(100000):
        overlap = False
        grid = [[False for x in range(size[0])] for y in range(size[1])]
        for robot in robots:
            for dir in range(2):
                robot["pos"][dir] = (robot["pos"][dir] + robot["vel"][dir]) % size[dir]
            if grid[robot["pos"][1]][robot["pos"][0]] == True:
                overlap = True
            grid[robot["pos"][1]][robot["pos"][0]] = True

       
        if overlap == False:
            for line in grid:
                for field in line:
                    if field:
                        print('#', end='')
                    else:
                        print('.', end='')
                print()
            print("Round: ", i + 1)
            break


main()