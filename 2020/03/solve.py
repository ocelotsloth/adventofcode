with open("input", "r") as file:
    lines = [line.strip() for line in file.readlines()]

def count(right, down):
    count = 0
    y = 0
    x = 0
    while y <= len(lines) - 1:
        if lines[y][x % len(lines[y])] == '#':
            count += 1
        y += down
        x += right
    return count

print("P1 TOTAL: ", count(3, 1))
partTwo = count(1, 1) * count(3, 1) * count(5, 1) * count(7, 1) * count(1, 2)
print("P2 MULT: ", partTwo)
