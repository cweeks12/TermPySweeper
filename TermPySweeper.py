import sys
import random

class TermPySweeper:
    def __init__(self, width, height, mines):
        self._field = []
        self._width = width
        self._height = height
        self._mines = mines

        for _ in range(height):
            temp = []
            for j in range(width):
                temp.append(False)
            self._field.append(temp)

        for i in range(mines):
            column,row = random.randint(0,width-1), random.randint(0, height-1)
            while self._field[row][column]:
                column,row = random.randint(0,width-1), random.randint(0, height-1)
            self._field[row][column] = True

        #Generate a view of the nearby mines, and a mask for the viewed items
        self._playerView = []
        for rowCount, row in enumerate(self._field):
            newRow = []
            for columnCount, item in enumerate(row):
                newRow.append('*' if item else self.getNumberOfSurroundingMines(rowCount, columnCount))
            self._playerView.append(newRow)

        self._playerViewMask = [ [False] * len(self._field[0]) ] * len(self._field)


        self.display()

    def getNumberOfSurroundingMines(self, i, j):
        count = 0
        for k in range(i-1, i+2):
            for l in range (j-1, j+2):
                if k < 0 or k > self._height - 1 or l < 0 or l > self._width-1:
                    continue
                count += 1 if self._field[k][l] else 0
        return str(count) if count > 0 else ' '

    def display(self):
        for row in self._field:
            for spot in row:
                print('X' if spot else '-', end='')
            print()

        for i, row in enumerate(self._playerView):
            for j, spot in enumerate(row):
                print(spot if self._playerViewMask[i][j] else '#', end='')
            print()



    def click(self, x, y):
        pass

if __name__ == '__main__':
    tps = TermPySweeper(15, 10, 15)
