from MazePackage import mazeGenerator
from MazePackage import mazeStarter

rowDimen = 0
colDimen = 0
rowDimen, colDimen = mazeStarter.getGameMatrixDimentions()

if (rowDimen<3 or colDimen<3) or (rowDimen>20 or colDimen>20) :
    print('Game can not be start! May be it is canceled by user.!')  
else:
    mazeObject = mazeGenerator.MazeClass(rowDimen, colDimen)
    userPress = str(input("If you understand the game guide table Press Y for start game, else press N for show game guide table again or press N for quit) (Y/N/Q): ")).lower()
    while userPress != 'y' or userPress != 'n' or userPress != 'q':
        match userPress:
            case 'y':
                print('Game started...')
                break
            case 'n':
                mazeObject.mazeDrawTableHelp(True)
                userPress = str(input("Press Y for start game, N for show guide table and Q for quit) (Y/N/Q): ")).lower()
            case 'q':
                print('Good by...!')
                break
            case _:
                mazeObject.mazeDrawTableHelp(True)
                userPress = str(input("Press Y for start game, N for show guide table and Q for quit) (Y/N/Q): ")).lower()
    if userPress == 'y':
        mazeObject.play()






