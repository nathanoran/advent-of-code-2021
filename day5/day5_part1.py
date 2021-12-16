inputFile = open("day5/input.txt", "r")

startX = []
startY = []
endX = []
endY = []

maxIndex = 0

for line in inputFile:
    startPoint, endPoint = line.strip().split(" -> ")

    sX, sY = [int(call) for call in startPoint.split(",")]
    eX, eY = [int(call) for call in endPoint.split(",")]

    if sX == eX or sY == eY:
        maxIndex = max(maxIndex, sX, sY, eX,eY)

        startX.append(sX)
        startY.append(sY)
        endX.append(eX)
        endY.append(eY)

seaFloor = []

# print(seaFloor)

for i in range(maxIndex + 1):
    seaFloor.append([])
    for j in range(maxIndex + 1):
        seaFloor[i].append(0)

# print(seaFloor)

dangerZones = 0

for i in range(len(startX)):
    deltaY = endY[i] - startY[i]
    deltaX = endX[i] - startX[i]

    if deltaY == 0:
        for x in range(min(startX[i], endX[i]), max(startX[i], endX[i]) + 1):
            seaFloor[x][startY[i]] += 1
            if seaFloor[x][startY[i]] == 2:
                dangerZones += 1

    if deltaX == 0:
        for y in range(min(startY[i], endY[i]), max(startY[i], endY[i]) + 1):
            seaFloor[startX[i]][y] += 1
            if seaFloor[startX[i]][y] == 2:
                dangerZones += 1

print(dangerZones)