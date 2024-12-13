f = open("input.txt", "r")

left = []
right = []

for line in f:
    x = list(map(int, line.split()))
    left.append(x[0])
    right.append(x[1])

left.sort()
right.sort()

result = 0
for x, y in zip(left, right):
    result += abs(x - y)

print(result)