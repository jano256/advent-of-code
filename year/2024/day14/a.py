def main():
    robots = []
    size = [101, 103]
    for line in open("input.txt", "r"):
        pos, vel = line.split()
        pos = list(map(int, pos[2:].split(',')))
        vel = list(map(int, vel[2:].split(',')))
        robots.append({"pos": pos, "vel": vel})
    
    quadrant = [0, 0, 0, 0]
    for robot in robots:
        for dir in range(2):
            robot["pos"][dir] = (robot["pos"][dir] + 100 * robot["vel"][dir]) % size[dir]

        if   robot["pos"][0] > size[0] // 2 and robot["pos"][1] > size[1] // 2:
            quadrant[0] += 1
        elif robot["pos"][0] > size[0] // 2 and robot["pos"][1] < size[1] // 2:
            quadrant[1] += 1
        elif robot["pos"][0] < size[0] // 2 and robot["pos"][1] > size[1] // 2:
            quadrant[2] += 1
        elif robot["pos"][0] < size[0] // 2 and robot["pos"][1] < size[1] // 2:
            quadrant[3] += 1

    sum = 1
    for i in quadrant:
        sum *= i
    print(sum)
    

main()