def main():
    blocklist = []
    max = 0
    with open("test.txt", "r") as f:
        disk_map = f.read()

    for i in range(len(disk_map)):
        if i % 2:
            blocklist.extend(int(disk_map[i]) * '.')
        else:
            blocklist.extend(int(disk_map[i]) * [i//2])
    else:
        max = i//2
    

    while True:
        left = blocklist.index('.')
        right = len(blocklist) - 1 - blocklist[::-1].index(max)
        if left > right:
            max -= 1
        else:
            blocklist[left], blocklist[right] = blocklist[right], blocklist[left]
        if max < 0:
            break


    checksum = 0
    for i in range(len(blocklist)):
        if blocklist[i] == '.':
            break
        checksum += blocklist[i] * i

    print(checksum)
    

main()