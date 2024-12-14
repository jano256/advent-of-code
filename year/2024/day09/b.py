def main():
    blocklist = []
    max = 0
    with open("input.txt", "r") as f:
        disk_map = f.read()

    for i in range(len(disk_map)):
        if i % 2:
            blocklist.extend(int(disk_map[i]) * '.')
        else:
            blocklist.extend(int(disk_map[i]) * [i//2])
    else:
        max = i//2
    

    for number in range(max, 0, -1):
        right = blocklist.index(number)
        len_right = len(blocklist) - 1 - blocklist[::-1].index(number) - right + 1
        left = 0
        for i in range(len(blocklist)):
            if blocklist[i] == '.':
                for length in range(len_right):
                    if blocklist[i + length] != '.':
                        i += length
                        break
                else:
                    left = i
                    break
            if i >= right:
                break

        if left != 0:
            for i in range(len_right):
                blocklist[left+i], blocklist[right+i] = blocklist[right+i], blocklist[left+i]


    checksum = 0
    for i in range(len(blocklist)):
        if blocklist[i] == '.':
            continue
        checksum += blocklist[i] * i
    print(checksum)
    

main()