def getGameMatrixDimentions(): 
    temp = 'q'
    getMatrixRowDimen = 0
    getMatrixColumnDimen = 0
    while True:
        try:
            temp = input('Enter Game Dimetion (ROW). (Number 3-20) (Q=Quit): ')
            getMatrixRowDimen = int(temp)
        except ValueError:
            if temp.lower() == 'q':
                print('Game canceled by user.!')
                break
            else: 
                print("Please enter a VALID Integer Number from 3 to 20 ")
                continue

        if getMatrixRowDimen >= 3 and getMatrixRowDimen <= 20:
            break
        else:
            print('The integer must be in the range 3...20')
    return getMatrixRowDimen, getMatrixRowDimen
