def main():
    final_sum = 0
    for line in open("input.txt", "r"):
        line = line.split()
        final_sum += calc(int(line[0][:-1:]), list(map(int, line[1::])))
    print(final_sum)
        

def calc(result, values):
    num_values = len(values)
    num_calcs = 3 ** (num_values - 1)

    for calc in range(num_calcs):
        sum = values[0]
        for i in range(1, len(values)):
            op = calc % 3
            if op == 0:
                sum += values[i]
            elif op == 1:
                sum *= values[i]
            else:
                sum = int(str(sum) + str(values[i]))
            calc //= 3
        if sum == result:
            return sum
    return 0


main()