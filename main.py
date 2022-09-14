import math
from random import random, randrange


board = []

def randomNumb():
    random1 = randrange(0,3)
    random2 = randrange(0,3)
    listRand = [random1, random2]
    return listRand

def alreadyPlayed(check):

    if check =='O' or check =='X':
        return True
    else: 
        return False

def computerPlay():     

    a = False
    while a == False:
        rand = randomNumb()
        random1, random2 =  rand
        check = board[random1][random2]
        played = alreadyPlayed(check)
        if played == False:
            a = True
        
        #print (random1, random2,'B')
    board[random1][random2] = 'X'

def buildNewBoard():
    cont = 0 
    for i in range (3):
        
        if cont == 0:
            row = [i for i in range (1,4)]
            cont +=1
        elif cont == 1:
            row = [i for i in range (4,7)]
            cont +=1
        else: 
            row = [i for i in range (7,10)]
        board.append(row)
    board[1][1] = 'X'
    print( '+-------+-------+-------+' )
    print( '|       |       |       |' )
    print( '|   ',board[0][0],'   |   ', board[0][1],'   |   ', board[0][2], '   |', sep = '' )
    print( '|       |       |       |' )
    print( '+-------+-------+-------+' )
    #Second
    
    print( '|       |       |       |' )
    print( '|   ',board[1][0],'   |   ', board[1][1],'   |   ', board[1][2], '   |', sep = '' )
    print( '|       |       |       |' )
    
    #Third
    print( '+-------+-------+-------+' )
    print( '|       |       |       |' )
    print( '|   ',board[2][0],'   |   ', board[2][1],'   |   ', board[2][2], '   |', sep = '' )
    print( '|       |       |       |' )
    print( '+-------+-------+-------+' )
    gameStarts()

def gameStarts():

    userTurn = int(input('Seleccione el numero donde desea poner su O: '))   

    while userTurn not in range(1,10):
        print ('Por favor introduzca un numero entre 1 a 9')
        userTurn = int(input('Seleccione el numero donde desea poner su O: '))
    if userTurn in range(1,10):
        cuadro = target(userTurn)
        #print (cuadro,'cuadro')
        data1, data2 = cuadro
        comprobar = board[data1][data2]
        #print(comprobar)
        played = alreadyPlayed(comprobar)
        if played == False:
            board[data1][data2] = 'O'
            pcMove = computerPlay()  
            printBoard()
        else: 
            print('Selecciona una casilla que no este en uso')
            gameStarts()

def printBoard():
    print( '+-------+-------+-------+' )
    print( '|       |       |       |' )
    print( '|   ',board[0][0],'   |   ', board[0][1],'   |   ', board[0][2], '   |', sep = '' )
    print( '|       |       |       |' )
    print( '+-------+-------+-------+' )
    #Second
    
    print( '|       |       |       |' )
    print( '|   ',board[1][0],'   |   ', board[1][1],'   |   ', board[1][2], '   |', sep = '' )
    print( '|       |       |       |' )
    
    #Third
    print( '+-------+-------+-------+' )
    print( '|       |       |       |' )
    print( '|   ',board[2][0],'   |   ', board[2][1],'   |   ', board[2][2], '   |', sep = '' )
    print( '|       |       |       |' )
    print( '+-------+-------+-------+' )
    gameStarts()

def target(userTurn):
    if userTurn == 1:
        a = board[0][0]
        data = [0,0]
        return data
    else:     
        row = math.ceil((userTurn/3))
        #print (row)

    if row <= 1:
        a = board[row-1][userTurn-1]
        data = [row-1, userTurn-1]
        return data
    elif row == 2:
        a = board[row-1][userTurn-4]
        data = [row-1, userTurn-4]
        return data
    elif row == 3:
        a = board[row-1][userTurn-7]
        data = [row-1, userTurn-7]
        return data

def alreadyWon():
    a = 'what'

buildNewBoard()