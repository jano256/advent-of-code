import re

def main():
    sum = 0
    with open("input.txt", "r") as f:
        data = f.read()

    muls = re.findall("mul\(\d+,\d+\)", data)
    for ex in muls:
        nums = re.findall("\d+", ex)
        sum += int(nums[0]) * int(nums[1])

    print(sum)

main()