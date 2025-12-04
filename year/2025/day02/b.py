def main():
    ID_Ranges = open("input.txt", "r").read().split(',')
    invalid_sum = 0
    for ID_Range in ID_Ranges:
        low, up = map(int, ID_Range.split('-'))
        for ID in map(str, range(low, up + 1)):
            length = len(ID)
            for size in range(1, length // 2 + 1):
                first = ID[:size]
                for block in range(0, length, size):
                    if (first != ID[block:block+size]):
                        break
                else:
                    invalid_sum += int(ID)
                    break            
    print(invalid_sum)
main()