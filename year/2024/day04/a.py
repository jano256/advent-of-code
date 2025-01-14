import re

def main():
    wordgrid = []
    for line in open("input.txt", "r"):
        wordgrid.append(line[:-1])
    print(wordgrid)

    x_len = len(wordgrid[0])
    y_len = len(wordgrid)

    cols = [[] for _ in range(x_len)]
    rows = [[] for _ in range(y_len)]
    diag1 = [[] for _ in range(y_len + x_len - 1)]
    diag2 = [[] for _ in range(len(diag1))]
    
    for x in range(x_len):
        for y in range(y_len):
            cols[x].append(wordgrid[y][x])
            rows[y].append(wordgrid[y][x])
            diag1[x + y].append(wordgrid[y][x])
            diag2[x - y + y_len - 1].append(wordgrid[y][x])

    found = 0
    for words in cols + rows + diag1 + diag2:
        found += len(re.findall("XMAS", "".join(words)))
        found += len(re.findall("SAMX", "".join(words)))
    print(found)


main()