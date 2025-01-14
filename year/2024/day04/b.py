import re
from itertools import chain

def main():
    wordgrid = []
    for line in open("input.txt", "r"):
        wordgrid.append(line[:-1])

    hits = 0
    for x in range(1, len(wordgrid[0]) - 1):
        for y in range(1, len(wordgrid) - 1):
            if wordgrid[y][x] == 'A' \
            and ((wordgrid[y-1][x-1] == 'M' and wordgrid[y+1][x+1] == 'S') or (wordgrid[y-1][x-1] == 'S' and wordgrid[y+1][x+1] == 'M')) \
            and ((wordgrid[y-1][x+1] == 'M' and wordgrid[y+1][x-1] == 'S') or (wordgrid[y-1][x+1] == 'S' and wordgrid[y+1][x-1] == 'M')):
                hits += 1
    print(hits)

main()