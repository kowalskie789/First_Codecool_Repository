from msilib.schema import tables
from operator import truediv
import re


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

    move = input("Whats your next move?").upper()
    while move not in 'A1,A2,A3,B1,B2,B3,C1,C2,C3'.split(","): #dodać drugi warunek:P
        move = input("Incorecct. Whats your next move?").upper()
    if move[0] == 'A':  
        if move[1] == '1':
            return [0,0]
        elif move[1] == '2':
            return [0,1]
        else:
            return [0,2]
    elif move[0] == 'B': 
        if move[1] == '1':
            return [1,0]
        elif move[1] == '2':
            return [1,1]
        else:
            return [1,2]
    if move[0] == 'C':
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
        get_winning_player()
        if is_board_full(tablica): #to na chwilkę tutaj będzie 
            quit()
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

def get_winning_player():
    if tablica[0][0]==tablica[0][1]==tablica[0][2] and tablica[0][0]!='.':
        return print("Wygrał ",tablica[0][0]) # to może zmienić na kejsy to może będzie ładniej i dodać quit() albo main menu
    if tablica[1][0]==tablica[1][1]==tablica[0][2] and tablica[1][0]!='.':
        return print("Wygrał ",tablica[1][0])
    if tablica[2][0]==tablica[2][1]==tablica[2][2] and tablica[2][0]!='.':
        return print("Wygrał ",tablica[2][0])
    if tablica[0][0]==tablica[1][0]==tablica[2][0] and tablica[0][0]!='.':
        return print("Wygrał ",tablica[0][0])
    if tablica[0][1]==tablica[1][1]==tablica[2][1] and tablica[0][1]!='.':
        return print("Wygrał ",tablica[0][1])
    if tablica[0][2]==tablica[1][2]==tablica[2][2] and tablica[0][2]!='.':
        return print("Wygrał ",tablica[0][2])
    if tablica[0][0]==tablica[1][1]==tablica[2][2] and tablica[0][0]!='.':
        return print("Wygrał ",tablica[0][0])
    if tablica[0][2]==tablica[1][1]==tablica[2][0] and tablica[0][2]!='.':
        return print("Wygrał ",tablica[0][2])
    
def is_board_full(table):
    if not any("." in x for x in table): #nie wiem jak to działa 
        print("tablica pełna koniec gry")
        return True
    return False



onevone()