def main():
    banks = open("input.txt", "r").read().split()
    sum = 0
    for bank in banks:
        bat1pos = find_big_pos(bank[:-1])
        bat2pos = find_big_pos(bank[bat1pos + 1:])
        sum += int(bank[bat1pos]) * 10 + int(bank[bat1pos + bat2pos + 1])
    print(sum)


def find_big_pos(bank):
    for jolt in map(str, range(9, 0, -1)):
        i = bank.find(jolt)
        if i >= 0:
            return i


main()