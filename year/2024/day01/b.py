f = open("input.txt", "r")

left = []
right = []

for line in f:
    x = list(map(int, line.split()))
    left.append(x[0])
    right.append(x[1])

result = 0
for i in left:
    result += i * right.count(i)

print(result)