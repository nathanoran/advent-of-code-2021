inputFile = open("day1/input.txt", "r")

sonarReading = []

for line in inputFile:
    sonarReading.append(int(line))

# print(sonarReading)

count = 0
i = 0
prev = 9999999999999

while i < len(sonarReading) - 2:
    current = sonarReading[i] + sonarReading[i+1] + sonarReading[i+2]

    # print(current)

    if current > prev:
        count += 1

    prev = current

    i += 1

print(count)