from pprint import pp
import tabulate as tablePrint
import random

class MazeClass():

    def __init__(self, mazeRow, mazeColumn):
        self.row = mazeRow
        self.column = mazeColumn
        self.name = type(self).__name__
        lst = []
        Maze = []
        counter = 0
        for row in range(mazeRow):
            for column in range(mazeColumn):
                lst.append({counter:[None, 0, 0]})
                counter+=1
            Maze.append(lst)
            lst = []
        self.baseMaze = Maze
        print('Game Help table:')
        self.mazeDrawTableHelp(True)
    
    def findBestCell(self):
        #خانه های اولین ستون با افزایش یک واحدی در شمارنده، مسیر طلایی هست
        #به عبارتی تکمیل شدن یک سطر کامل توسط یک بازیکن او را برنده می کند
        counter = 0
        xCounter = 0
        oCounter = 0 
        emptyRow = 0
        emptyColumn = 0
        emptyCounter = 0
        for row in range(self.row):
            for column in range(self.column):
                if str(self.baseMaze[row][column][counter][0]) == 'X':
                    xCounter+=1
                elif str(self.baseMaze[row][column][counter][0]) == 'O':
                    oCounter+=1
                else:
                    emptyRow = row
                    emptyColumn = column
                    emptyCounter = counter
                counter += 1
            if xCounter == self.column - 1 and oCounter==0:
                self.baseMaze[emptyRow][emptyColumn][emptyCounter][0] = 'X'
                self.calculate_AllCells_SumScores()
                self.mazeDrawTableHelp(False)
                print('Takmil shodane SATR ba X')
                return 'The X player is WON :)'
            elif oCounter == self.column - 1 and xCounter==0: 
                self.baseMaze[emptyRow][emptyColumn][emptyCounter][0] = 'X'
                self.calculate_AllCells_SumScores()
                self.mazeDrawTableHelp(False)
                print('Bastane Masire Barande Shodane Satriye O!')
                return'Bastane Masire Barande Shodane Satriye O!'
            xCounter = 0
            oCounter = 0
            emptyRow = 0
            emptyColumn = 0
            emptyCounter = 0
                
        #خانه های اولین سطر با مقدار پرش تعدادکل ستونهای کلی در شمارنده، مسیر طلایی هست
        #به عبارتی تکمیل شدن یک ستون کامل توسط یک بازیکن باعث برنده شدن او می شود
        counter = 0
        xCounter = 0
        oCounter = 0
        emptyRow = 0
        emptyColumn = 0
        emptyCounter = 0
        for column in range(self.column):
            counter = column
            for row in range(self.row):
                if str(self.baseMaze[row][column][counter][0]) == 'X':
                    xCounter+=1
                elif str(self.baseMaze[row][column][counter][0]) == 'O':
                    oCounter+=1
                else:
                    emptyRow = row
                    emptyColumn = column
                    emptyCounter = counter
                counter += self.column
            if xCounter == self.column - 1 and oCounter==0:
                self.baseMaze[emptyRow][emptyColumn][emptyCounter][0] = 'X'
                self.calculate_AllCells_SumScores()
                self.mazeDrawTableHelp(False)
                print('Takmil shodane SOOTOON ba X')
                return 'The X player is WON :)'
            elif oCounter == self.column - 1 and xCounter==0:
                self.baseMaze[emptyRow][emptyColumn][emptyCounter][0] = 'X'
                self.calculate_AllCells_SumScores()
                self.mazeDrawTableHelp(False)
                print('Bastane Masire Barande Shodane Sootooniye O!')
                return'Bastane Masire Barande Shodane Sootooniye O!'
            xCounter = 0
            oCounter = 0
            emptyRow = 0
            emptyColumn = 0
            emptyCounter = 0

        #خانه های درایه اصلی مورب یعنی شروع از کورنر بالا چپ با افزایش کل تعداد ستونها+1 واحدی در شمارنده، مسیر طلایی هست
        #به عبارتی تکمیل شدن درایه توسط یک بازیکن او را برنده می کند
        counter = 0
        xCounter = 0
        oCounter = 0
        emptyRow = 0
        emptyColumn = 0
        emptyCounter = 0
        for row in range(self.row):
            for column in range(self.column):
                if str(self.baseMaze[row][column][counter][0]) == 'X' and row == column:
                    xCounter+=1
                elif str(self.baseMaze[row][column][counter][0]) == 'O' and row == column:
                    oCounter+=1
                elif str(self.baseMaze[row][column][counter][0]) != 'X' and str(self.baseMaze[row][column][counter][0]) != 'O' and row==column:
                    emptyRow = row
                    emptyColumn = column
                    emptyCounter = counter
                counter = counter + 1
        if xCounter == ((self.row + self.column) / 2) - 1 and oCounter==0:
            self.baseMaze[emptyRow][emptyColumn][emptyCounter][0] = 'X'
            self.calculate_AllCells_SumScores()
            self.mazeDrawTableHelp(False)
            print('Takmil shodane DERAYE ASLIye Matrix')
            return'The X player is WON :)'
        elif oCounter == ((self.row + self.column) / 2) - 1 and xCounter==0:
            self.baseMaze[emptyRow][emptyColumn][emptyCounter][0] = 'X'
            self.calculate_AllCells_SumScores()
            self.mazeDrawTableHelp(False)
            print('Bastane Masire Barande Shodane Deraye Aliye O!')
            return'Bastane Masire Barande Shodane Deraye Aliye O!'
        xCounter = 0
        oCounter = 0
        emptyRow = 0
        emptyColumn = 0
        emptyCounter = 0

        #خانه های درایه فرعی مورب یعنی شروع از کورنر بالا راست با افزایش کل تعداد ستونها-1 واحدی در شمارنده، مسیر طلایی هست
        #به عبارتی تکمیل شدن درایه فرعی توسط یک بازیکن او را برنده می کند
        counter = 0
        xCounter = 0
        oCounter = 0
        emptyRow = 0
        emptyColumn = 0
        emptyCounter = 0
        for row in range(self.row):
            for column in range(self.column):
                if str(self.baseMaze[row][column][counter][0]) == 'X' and column == self.column-row-1:
                    xCounter+=1
                elif str(self.baseMaze[row][column][counter][0]) == 'O' and column == self.column-row-1:
                    oCounter+=1
                elif str(self.baseMaze[row][column][counter][0]) != 'X' and str(self.baseMaze[row][column][counter][0]) != 'O' and column == self.column-row-1:
                    emptyRow = row
                    emptyColumn = column
                    emptyCounter = counter
                counter = counter + 1
        if xCounter == ((self.row + self.column) / 2) - 1 and oCounter==0:
            self.baseMaze[emptyRow][emptyColumn][emptyCounter][0] = 'X'
            self.calculate_AllCells_SumScores()
            self.mazeDrawTableHelp(False)
            print('Takmil shodane DERAYE Fariye Matrix')
            return'The X player is WON :)'
        elif oCounter == ((self.row + self.column) / 2) - 1 and xCounter==0:
            self.baseMaze[emptyRow][emptyColumn][emptyCounter][0] = 'X'
            self.calculate_AllCells_SumScores()
            self.mazeDrawTableHelp(False)
            print('Bastane Masire Barande Shodane Deraye Fariye O!')
            return'Bastane Masire Barande Shodane Deraye Fariye O!'
        xCounter = 0
        oCounter = 0
        emptyRow = 0
        emptyColumn = 0
        emptyCounter = 0


        #یافتن بهترین خانه با یافتن خانه ای با بیشترین امتیاز حریف در آن خانه
        counter = 0
        maxioRow = 0
        maxioColumn = 0
        maxioCounter = 0
        maxioPosition = 0
        maxioHolderMaxValue = 0
        for row in range(self.row):
            for column in range(self.column):
                if str(self.baseMaze[row][column][counter][0]) != 'O' and self.baseMaze[row][column][counter][0] != 'X' and self.baseMaze[row][column][counter][2] > maxioHolderMaxValue: 
                    maxioRow = row
                    maxioColumn = column
                    maxioCounter = counter
                    maxioPosition = self.baseMaze[row][column][counter]
                    maxioHolderMaxValue = self.baseMaze[row][column][counter][2]
                counter+=1
        self.baseMaze[maxioRow][maxioColumn][maxioCounter][0] = 'X'

        self.calculate_AllCells_SumScores()
        self.mazeDrawTableHelp(False)
        print('Yaftane Cell ba Bishtarin Emtiyaze O va gozashtane X dar An!')
        return'Yaftane Cell ba Bishtarin Emtiyaze O va gozashtane X dar An!' 
                

    #محاسبه امتیازات هر خانه بر اساس مقادیر خانه های همجوار
    def calculate_AllCells_SumScores(self):
        counter = 0
        maxCol = self.column
        maxRow = self.row
        for row in range(self.row):
            for column in range(self.column):
                self.baseMaze[row][column][counter][1] = 0
                self.baseMaze[row][column][counter][2] = 0
                if row == 0:
                    if column == 0: #C1                        
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column+1][counter+maxCol+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column+1][counter+maxCol+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                    elif column == maxCol-1: #C2
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column-1][counter+maxCol-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column-1][counter+maxCol-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                    else: #A
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column-1][counter+maxCol-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column+1][counter+maxCol+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column-1][counter+maxCol-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column+1][counter+maxCol+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                elif row == maxRow-1:
                    if column == 0: #C3
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column+1][counter-maxCol+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row-1][column+1][counter-maxCol+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                    elif column == maxCol-1: #C4
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column-1][counter-maxCol-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row-1][column-1][counter-maxCol-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                    else: #B
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column-1][counter-maxCol-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column+1][counter-maxCol+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row-1][column-1][counter-maxCol-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row-1][column+1][counter-maxCol+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                else:
                    if column == 0: #C5
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column+1][counter-maxCol+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column+1][counter+maxCol+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row-1][column+1][counter-maxCol+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column+1][counter+maxCol+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                    elif column == maxCol-1: #C6
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column-1][counter-maxCol-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column-1][counter+maxCol-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row-1][column-1][counter-maxCol-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column-1][counter+maxCol-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                    else: #E
                        if str(self.baseMaze[row-1][column-1][counter-maxCol-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column+1][counter-maxCol+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column-1][counter+maxCol-1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row+1][column+1][counter+maxCol+1][0]) == 'X': self.baseMaze[row][column][counter][1]+=1
                        if str(self.baseMaze[row-1][column-1][counter-maxCol-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row-1][column][counter-maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row-1][column+1][counter-maxCol+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row][column-1][counter-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row][column+1][counter+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column-1][counter+maxCol-1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column][counter+maxCol][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                        if str(self.baseMaze[row+1][column+1][counter+maxCol+1][0]) == 'O': self.baseMaze[row][column][counter][2]+=1
                counter+=1


    def mazeDrawTableHelp(self, blank):
        if blank: print(f"\n\n\n")
        forPrintRow = []
        forPrintCol = []
        counter = 0
        for row in range(self.row):
            for column in range(self.column):
                if str(self.baseMaze[row][column][counter][0]) == 'X' or str(self.baseMaze[row][column][counter][0]) =='O':
                    forPrintRow.append(str(self.baseMaze[row][column][counter][0]))
                else:
                    if not blank:
                        forPrintRow.append(str(chr(46)))
                    else:
                        forPrintRow.append(str(counter))
                counter+=1
            forPrintCol.append(forPrintRow)
            forPrintRow = []
        if blank:
            print("+-------------------------------------------------------------------------+")
            print("|                Mehdi Samee Rad's Maze Game Guide Table                  |")
            print("+-------------------------------------------------------------------------+")
            print("| Welcome to this game. This MAZE GAME is simple textbase game in Python! |")
            print("| Game will be started is randomly by Computer (Player 1) with 'X' sign.  |")
            print("| Computer (Player 1) flag sign is 'X'.                                   |")
            print("| Your (Player 2) flag sign is 'O'.                                       |")
            print("| Contact: +98 914 157 4579                                               |")
            print("| Good luck and win!  :-)                                                 |")
            print("+-------------------------------------------------------------------------+")
            getHelpRequest = False
        print(tablePrint.tabulate(forPrintCol, tablefmt="grid"))


    def checkFilling(self):
        #تست پر شدن ماتریس
        filled = True
        counter = 0
        for row in range(self.row):
            for column in range(self.column):
                if str(self.baseMaze[row][column][counter][0]) != 'X' and str(self.baseMaze[row][column][counter][0]) != 'O':
                    filled = False
                counter+=1
        return filled

    def checkWinner(self):
        winner = '' 
        counter = 0
        xCounter = 0
        oCounter = 0
        for row in range(self.row):
            for column in range(self.column):
                if str(self.baseMaze[row][column][counter][0]) == 'X':
                    xCounter+=1
                elif str(self.baseMaze[row][column][counter][0]) == 'O':
                    oCounter+=1
                counter += 1
            if xCounter == self.column:
                winner='X'
            elif oCounter == self.column:
                winner='O'
            xCounter = 0
            oCounter = 0
        if winner != "": 
            print(f"The {winner} player is Won in Satri")
            return winner
        #----------------------------------
        counter = 0
        xCounter = 0
        oCounter = 0
        for column in range(self.column):
            counter = column
            for row in range(self.row):
                if str(self.baseMaze[row][column][counter][0]) == 'X':
                    xCounter+=1
                elif str(self.baseMaze[row][column][counter][0]) == 'O':
                    oCounter+=1
                counter += self.column
            if xCounter == self.column:
                winner='X'
            elif oCounter == self.column:
                winner='O'
            xCounter = 0
            oCounter = 0
        if winner != "": 
            print(f"The {winner} player is Won in Sootooni")
            return winner
        #---------------------------------
        counter = 0
        xCounter = 0
        oCounter = 0
        for row in range(self.row):
            for column in range(self.column):
                if str(self.baseMaze[row][column][counter][0]) == 'X' and row == column:
                    xCounter+=1
                elif str(self.baseMaze[row][column][counter][0]) == 'O' and row == column:
                    oCounter+=1
                counter = counter + 1
        if xCounter == ((self.row + self.column) / 2):
            winner='X'
        elif oCounter == ((self.row + self.column) / 2):
            winner='O'
        xCounter = 0
        oCounter = 0
        if winner != "": 
            print(f"The {winner} player is Won in Deraye ASLI")
            return winner
        #--------------------------------
        counter = 0
        xCounter = 0
        oCounter = 0
        for row in range(self.row):
            for column in range(self.column):
                if str(self.baseMaze[row][column][counter][0]) == 'X' and column == self.column-row-1:
                    xCounter+=1
                elif str(self.baseMaze[row][column][counter][0]) == 'O' and column == self.column-row-1:
                    oCounter+=1
                counter = counter + 1
        if xCounter == ((self.row + self.column) / 2):
            winner='X'
        elif oCounter == ((self.row + self.column) / 2):
            winner='O'
        xCounter = 0
        oCounter = 0
        if winner != "": 
            print(f"The {winner} player is Won in Deraye Farei")
            return winner

        return winner
        

    def play(self):
        #اولین انتخاب در شروع بازی توسط رایانه و بصورت تصادفی می باشد
        startPosition = random.randint(0, (self.row * self.column)-1)
        placeHolder = 0
        for row in range(self.row):
            for column in range(self.column):
                if placeHolder == startPosition:
                    self.baseMaze[row][column] = {placeHolder: ['X', 0, 0]}
                placeHolder+=1   
        mess = ''
        
        busyCellNumberPressed = False

        while True:

            self.mazeDrawTableHelp(False)

            if busyCellNumberPressed == False:
                self.calculate_AllCells_SumScores()
            else:
                busyCellNumberPressed = False


            #بررسی پر شدن جدول بدون برنده
            if self.checkFilling() == True:
                print('The GAME Table is Filled and Game is Over!!!. Players are POTs.')
                break

            #بررسی شخص برنده
            elif (self.checkWinner() == 'O' or self.checkWinner() == 'X'):
                winner = ''
                if self.checkWinner() == 'O':
                    winner = 'Your (O)'
                if self.checkWinner() == 'X':
                    winner = 'Computer (X)'
                print(f'{winner} is wwwiiinnn!!! and Game is finished.')
                break

            userEntered = input(f'Enter the cell number of your choice. Your flag is O, Computer flag is X. {mess}(Number 0-{(self.row*self.column)-1}) , Q=Quit, H=Help): ')
            mess = ''

            if userEntered.lower() == 'q':
                print('Game is canceled by the user and it is Finished.')
                break #خروج از وایل اصلی
            elif userEntered.lower() == 'h':
                self.mazeDrawTableHelp(True)
            else:
                try:
                    numberSelectedUser = int(userEntered)
                except ValueError:
                    mess = "A valid integer. "
                    continue #عدم اجرای ادامه برنامه و بازگشت به اول وایل

                if (numberSelectedUser >= 0 and numberSelectedUser < self.row*self.column):
                    counter = 0
                    for row in range(self.row):
                        for column in range(self.column):
                            #بررسی پر بودن خانه از قبل
                            if (str(self.baseMaze[row][column][counter][0]) == 'X' or str(self.baseMaze[row][column][counter][0]) =='O') and counter == numberSelectedUser:
                                busyCellNumberPressed = True
                                mess = f"Cell[{numberSelectedUser}] is busy! Please, select another cell. "
                            if self.baseMaze[row][column][counter][0] == None and counter == numberSelectedUser:
                                self.baseMaze[row][column][counter][0] = 'O'
                            counter+=1
                    
                    if busyCellNumberPressed == False:
                        self.calculate_AllCells_SumScores()
                        if self.findBestCell() == 'The X player is WON :)':
                            print('The X player is WON :)')
                            return

                else:
                    mess = f'The integer must be in the range 0-{(self.row*self.column)-1}. '
                    continue
        
