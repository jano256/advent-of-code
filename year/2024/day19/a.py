from functools import cache

def main():
    towels, designs = open("input.txt", "r").read().split("\n\n")
    towels = tuple(towels.split(", "))
    designs = tuple(designs.splitlines())

    matches = 0
    for design in designs:
        matches += find(design, towels)
    print(matches)

@cache
def find(design, towels):
    if len(design) == 0:
        return True
    
    found = False
    for towel in towels:
        if towel == design[:len(towel)] and find(design[len(towel):], towels):
            found = True
    return found


main()