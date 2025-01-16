def main():

    rules, pages = open("test.txt", "r").read().split("\n\n")
    rules = [tuple(map(int, i.split('|'))) for i in rules.splitlines()]
    pages = [tuple(map(int, i.split(','))) for i in pages.splitlines()]

main()