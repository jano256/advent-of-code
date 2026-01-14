def main():
    banks = open("input.txt", "r").read().split()
    sum = 0
    for bank in banks:
        last_pos = 0
        for battery in range(11, -1, -1):
            last_pos += find_big_pos(bank, last_pos, battery)
            sum += int(bank[last_pos]) * pow(10, battery)
            last_pos += 1
    print(sum)


def find_big_pos(bank, start, stop):
    for jolt in map(str, range(9, 0, -1)):
        if (stop == 0):
            i = bank[start:].find(jolt)
        else:
            i = bank[start:-stop].find(jolt)
        if i >= 0:
            return i


main()