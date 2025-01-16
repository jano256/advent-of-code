def main():

    rules, pages = open("input.txt", "r").read().split("\n\n")
    rules = [tuple(map(int, i.split('|'))) for i in rules.splitlines()]
    pages = [list(map(int, i.split(','))) for i in pages.splitlines()]

    solution = 0

    for page in pages:
        sorted = True
        i = 0
        while i < len(rules):
            left, right = rules[i]
            if left in page and right in page and page.index(left) > page.index(right):
                page[page.index(left)], page[page.index(right)] = page[page.index(right)], page[page.index(left)]
                sorted = False
                i = 0
                continue
            i += 1
        if not sorted:
            solution += page[len(page) // 2]

    print(solution)


main()