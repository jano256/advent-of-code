def main():
    f = open("test.txt", "r")
    safe = 0

    for line in f:
        val = list(map(int, line.split()))
        if test(val):
            safe += 1
        else:
            for i in range(len(val)):
                valshort = val.copy()
                valshort.pop(i)
                if test(valshort):
                    safe += 1
                    break
    print(safe)


def test(val):
    print(val)

    up = 1
    if val[1] - val[0] < 0:
        up = -1
    
    for i in range(1, len(val)):
        diff = val[i] - val[i-1]
        if diff * up > 3 or diff * up <= 0:
            return False
    else:
        return True

main()