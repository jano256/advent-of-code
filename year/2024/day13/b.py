import re

def main():
    machines = []
    with open("test.txt", "r") as f:
        for machine in f.read().split("\n\n"):
            machines.append(map(int, re.findall(r'\d+', machine)))

    total_cost = 0
    for ax, ay, bx, by, x, y in machines:
        x += 10000000000000
        y += 10000000000000
        win = False
        cost = 99999999
        for a in range(100):
            for b in range(100):
                cx = a * ax + b * bx
                cy = a * ay + b * by
                if cx == x and cy == y:
                    win = True
                    new_cost = 3 * a + b
                    if new_cost < cost:
                        cost = new_cost
        if win:
            total_cost += cost
    
    print(total_cost)

main()

'''
zwei linien, die sich treffen
a von 0/0 richung ziel, b von ziel richtung 0/0
wenn die punkte der linien sich treffen, ist es das ergebnis
'''