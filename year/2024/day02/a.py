f = open("input.txt", "r")

data = []
safe = 0

for line in f:
    val = list(map(int, line.split()))    
    up = 1
    if val[1] - val[0] < 0:
        up = -1
    
    for i in range(1, len(val)):
        diff = val[i] - val[i-1]
        if diff * up > 3 or diff * up <= 0:
            break
    else:
        safe += 1


print(safe)

