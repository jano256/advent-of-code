import re

def main():
    machines = []
    with open("input.txt", "r") as f:
        for machine in f.read().split("\n\n"):
            machines.append(map(int, re.findall(r'\d+', machine)))

    total_cost = 0
    for ax, ay, bx, by, x, y in machines:
        x += 10000000000000
        y += 10000000000000

        a = (x * by - y * bx) / (by * ax - bx * ay)
        b = (x * ay - y * ax) / (ay * bx - by * ax)
        
        if a % 1 == 0 and b % 1 == 0:
            total_cost += round(3 * a + b)
        
    print(total_cost)

main()