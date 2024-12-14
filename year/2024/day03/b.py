import re

def main():
    sum = 0
    enable = True

    with open("input.txt", "r") as f:
        data = f.read()

    muls = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
    for ex in muls:
        if ex == "do()":
            enable = True
        elif ex == "don't()":
            enable = False
        else:
            if enable:
                nums = re.findall("\d+", ex)
                sum += int(nums[0]) * int(nums[1])

    print(sum)

main()