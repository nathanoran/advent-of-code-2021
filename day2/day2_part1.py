inputFile = open("day2/input.txt", "r")

sonarReading = []

for line in inputFile:
    sonarReading.append(line)

# print(sonarReading)

position = 0
depth = 0
i = 0

while i < len(sonarReading):
    direction = sonarReading[i].split(" ")

    # print(direction)

    if direction[0] == 'forward':
        position += int(direction[1])
    elif direction[0] == 'down':
        depth += int(direction[1])
    elif direction[0] == 'up':
        depth -= int(direction[1])
        if depth < 0:
            depth = 0

    i += 1

print(position * depth)