class BingoCell:
    def __init__(self, value):
        self.value = value
        self.called = False

class WinState:
    def __init__(self, row):
        self.row = row
    
    def checkForWin(self, call):
        win = True
        for cell in self.row:
            cell.called |= (cell.value == call)
            win &= cell.called
        return win

class BingoCard:
    def __init__(self, rows):
        self.winStates = [WinState(row) for row in rows]
        for i in range(5):
            self.winStates.append(WinState([rows[0][i], rows[1][i], rows[2][i], rows[3][i], rows[4][i]]))

    def checkForWin(self, call):
        win = False
        for winState in self.winStates:
            win |= winState.checkForWin(call)
        return win

    def getBoardScore(self):
        score = 0
        for i in range(5):
            for cell in self.winStates[i].row:
                if not cell.called:
                    score += cell.value
        return score