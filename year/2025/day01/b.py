def main():
    rotations = list(map(int, open("input.txt", "r").read().replace('L', '-').replace('R', '').split()))
    dial = 50
    zerohits = 0

    for rotation in rotations:
        step = rotation // abs(rotation)
        for _ in range(abs(rotation)):
            dial += step
            if dial % 100 == 0:
                zerohits += 1
        
    print(zerohits)

main()