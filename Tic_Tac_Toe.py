from msilib.schema import tables
from operator import truediv


def get_board():
    return [[ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ]]
                  #A              #B              #C
#print(get_board()[2][0])
                  #C#1 

tablica = get_board() #ważne!!! 

def print_board():
    print("   1   2   3")
    print("A ",tablica[0][0],"|",tablica[0][1],"|",tablica[0][2],"")
    print("  ---+---+---")
    print("B ",tablica[1][0],"|",tablica[1][1],"|",tablica[1][2],"")
    print("  ---+---+---")
    print("C ",tablica[2][0],"|",tablica[2][1],"|",tablica[2][2],"")

def get_human_coordinates():

    move = input("Whats your next move?")
    while move not in 'A1,A2,A3,B1,B2,B3,C1,C2,C3,a1,a2,a3,b1,b2,b3,c1,c2,c3'.split(","): #dodać drugi warunek:P
        move = input("Incorecct. Whats your next move?")
    if move[0] == 'A' or move[0] == 'a': #to głupie może jakoś zmienić?  
        if move[1] == '1':
            return [0,0]
        elif move[1] == '2':
            return [0,1]
        else:
            return [0,2]
    elif move[0] == 'B' or move[0] == 'b': #to głupie może jakoś zmienić?  
        if move[1] == '1':
            return [1,0]
        elif move[1] == '2':
            return [1,1]
        else:
            return [1,2]
    if move[0] == 'C' or move[0] == 'c': #to głupie może jakoś zmienić?  
        if move[1] == '1':
            return [2,0]
        elif move[1] == '2':
            return [2,1]
        else:
            return [2,2]


def implement_move(coordinate,znak):
    tablica[coordinate[0]][coordinate[1]] = znak
    return

def onevone():
    X=True
    while True:
        print_board()
        while X:
            holder = get_human_coordinates()
            if tablica[holder[0]][holder[1]] not in "X,O".split(","):
                implement_move(holder,"X")
                X= False
                break
            else:
                print("Wrong move, try again")
        else:
            holder = get_human_coordinates()
            if tablica[holder[0]][holder[1]] not in "X,O".split(","):
                implement_move(holder,"O")
                X= True
            else:
                print("Wrong move, try again")
            

onevone()