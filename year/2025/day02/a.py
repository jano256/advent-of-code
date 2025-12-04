def main():
    ID_Ranges = open("input.txt", "r").read().split(',')
    invalid_sum = 0
    for ID_Range in ID_Ranges:
        low, up = map(int, ID_Range.split('-'))
        for ID in map(str, range(low, up + 1)):
            length = len(ID)
            if (length % 2):
                continue
            if (ID[:length // 2] == ID[length // 2:]):
                invalid_sum += int(ID)            
    print(invalid_sum)
main()