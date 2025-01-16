def main():

    rules, pages = open("input.txt", "r").read().split("\n\n")
    rules = [tuple(map(int, i.split('|'))) for i in rules.splitlines()]
    pages = [tuple(map(int, i.split(','))) for i in pages.splitlines()]

    solution = 0
    for page in pages:
        for left, right in rules:
            if left in page and right in page:
                if page.index(left) > page.index(right):
                    break
        else:
            solution += page[len(page) // 2]

    print(solution)

main()