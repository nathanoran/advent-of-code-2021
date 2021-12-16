inputFile = open("day6/input.txt", "r")

allLanternfish = []

for line in inputFile:
    allLanternfish = [int(fish) for fish in line.strip().split(",")]

# print(allLanternfish)

for x in range(80):
    for i in range(len(allLanternfish)):
        allLanternfish[i] -= 1
        if allLanternfish[i] < 0:
            allLanternfish.append(8)
            allLanternfish[i] = 6

print(len(allLanternfish))
