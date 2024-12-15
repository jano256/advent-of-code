from functools import cache

def main():
    with open("input.txt", "r") as f:
        stones = list(map(int, f.read().split()))

    stone_count = 0
    for stone in stones:
        stone_count += count(stone, 75)
    print(stone_count)

@cache
def count(stone, round):
    if round == 0:
        return 1
    
    if stone == 0:
        return count(1, round - 1)
    digits = len(str(stone))
    if digits % 2 == 0:
        return count(int(str(stone)[digits//2:]), round - 1) + count(int(str(stone)[:digits//2]), round - 1)
    return count(stone * 2024, round - 1)

main()