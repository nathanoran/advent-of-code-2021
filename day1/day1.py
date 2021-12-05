inputFile = open("day1/part1_input.txt", "r")

sonarReading = []

for line in inputFile:
    sonarReading.append(int(line))

# print(sonarReading)

sonarReading.reverse()

count = 0
prev = 9999999999999

while len(sonarReading) > 0:
    current = sonarReading.pop()

    # print(current)

    if current > prev:
        count += 1

    prev = current

print(count)