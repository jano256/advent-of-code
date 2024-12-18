import re

def main():
    with open("input.txt", "r") as f:
        read = list(map(int, re.findall(r'\d+', f.read())))
    a, b, c = read[:3]
    prog = read[3:]
    global out
    out = []

    print(a, b, c,"     ", prog)

    k = 0
    for j in range(0o1_035_510_040_000_000, 0o10_000_000_000_000_000, 0o1):
        out = []
        k += 1
        calc(j, b, c, prog)
        
        #print(oct(j), out)
        if prog == out:
            print("a should be: ", j)
            break
        if k == 8:
            pass
            #break


def calc(a, b, c, prog):
    i = 0
    prog_length = len(prog)

    while i < prog_length:
        instruction , literal = prog[i:i+2]
        combo = literal
        if literal > 3:
            combo = [a, b, c][combo-4]
        i += 2
        match instruction:
            case 0: a >>= combo
            case 1: b ^= literal
            case 2: b = combo % 8
            case 3 if a != 0: i = literal
            case 4: b ^= c
            case 5: out.append(combo % 8)
            case 6: b = a >> combo
            case 7: c = a >> combo

main()