from day4_classes import BingoCard
from day4_classes import BingoCell
from day4_classes import WinState

inputFile = open("day4/input.txt", "r")

bingoCalls = []
bingoCards = []

rowCount = 0
currentCard = []

firstLine = True

for line in inputFile:
    if firstLine:
        bingoCalls = [int(call) for call in line.split(",")]
        
        firstLine = False

    elif line.strip() == (""):
        rowCount = 0
        currentCard = []

    else:
        rowCount += 1
        currentCard.append([BingoCell(int(cell)) for cell in line.strip().split(" ")])

        if(rowCount == 5):
            bingoCards.append(BingoCard(currentCard))

#print(bingoCalls)

remainingSum = 0
winningCall = -1

for bingoCall in bingoCalls:
    if len(bingoCards) > 1:
        i = 0
        while i < len(bingoCards):
            if bingoCards[i].checkForWin(bingoCall):
                bingoCards.remove(bingoCards[i])
            else:
                i += 1
    elif winningCall == -1:
        if bingoCards[0].checkForWin(bingoCall):
            winningCall = bingoCall
            remainingSum = bingoCards[0].getBoardScore()

print(winningCall * remainingSum)