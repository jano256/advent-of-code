def main():
    with open("input.txt", "r") as f:
        stones = list(map(int, f.read().split()))

    for x in range(25):
        print(x)
        offset = 0
        for base in range(len(stones)):
            i = base + offset
            digits = len(str(stones[i]))
            if stones[i] == 0:
                stones[i] = 1
            elif digits % 2 == 0:
                stones.insert(i, int(str(stones[i])[:digits//2]))
                offset += 1
                i += 1
                stones[i] = int(str(stones[i])[digits//2:])
            else:
                stones[i] *= 2024
    print(len(stones))

main()