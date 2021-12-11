def splitOnesAndZeroes(report, index):
    ones =[]
    zeroes = []

    for diagnostic in report:
        if list(diagnostic)[index] == "1":
            ones.append(diagnostic)
        else:
            zeroes.append(diagnostic)

    return ones, zeroes

def findOxygenGeneratorRating(report, index, lineLen):
    if index == lineLen:
        return ""

    ones, zeroes = splitOnesAndZeroes(report, index)

    if len(ones) >= len(zeroes):
        return "1" + findOxygenGeneratorRating(ones, index+1, lineLen)
    else:
        return "0" + findOxygenGeneratorRating(zeroes, index+1, lineLen)

def findC02ScrubberRating(report, index, lineLen):
    if index >= lineLen:
        return ""

    ones, zeroes = splitOnesAndZeroes(report, index)
    
    if 0 < len(zeroes) <= len(ones):
        return "0" + findC02ScrubberRating(zeroes, index+1, lineLen)
    elif len(ones) <= 0:
        return "0" + findC02ScrubberRating(zeroes, index+1, lineLen)
    else:
        return "1" + findC02ScrubberRating(ones, index+1, lineLen)

def binaryListToNum(binaryList, lineLen):
    retVal = 0
    for binaryPlace in binaryList:
        if binaryPlace == "1":
            retVal += 2 ** (lineLen - 1)
    
        lineLen -= 1

    return retVal



inputFile = open("day3/input.txt", "r")

diagnosticReport = []

for line in inputFile:
    diagnosticReport.append(line)

# print(diagnosticReport)

lineLen = len(diagnosticReport[0]) - 1

oxygenGeneratorRating = binaryListToNum(
        list(findOxygenGeneratorRating(diagnosticReport, 0, lineLen)),
        lineLen
    )

c02ScrubberRating = binaryListToNum(
        list(findC02ScrubberRating(diagnosticReport, 0, lineLen)),
        lineLen
    )

print(oxygenGeneratorRating * c02ScrubberRating)