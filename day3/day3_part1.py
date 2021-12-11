inputFile = open("day3/input.txt", "r")

diagnosticReport = []

for line in inputFile:
    diagnosticReport.append(line)

lineLen = len(diagnosticReport[0]) - 1
diagnosticSumList = []

for x in range(lineLen):
    diagnosticSumList.append(0)
i = 0

while i < len(diagnosticReport):
    diagnostic = list(diagnosticReport[i])

    # print(diagnostic)

    j = 0

    while j < lineLen:
        diagnosticSumList[j] += int(diagnostic[j])
        j += 1

    # print(diagnosticSumList)

    i += 1

gamma = 0
epsilon = 0

for diagnosticSum in diagnosticSumList:
    if diagnosticSum / len(diagnosticReport) > 0.5:
        gamma += 2 ** (lineLen - 1)
    else:
        epsilon += 2 ** (lineLen - 1)
    
    lineLen -= 1

print(gamma * epsilon)
