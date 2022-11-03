import random
import time

def get_board():
    return [[ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ]]
                  #A              #B              #C
#print(get_board()[2][0])
                  #C#1 
#tablica = get_board()


def print_board():
    print("   1   2   3")
    print("A ",tablica[0][0],"|",tablica[0][1],"|",tablica[0][2],"")
    print("  ---+---+---")
    print("B ",tablica[1][0],"|",tablica[1][1],"|",tablica[1][2],"")
    print("  ---+---+---")
    print("C ",tablica[2][0],"|",tablica[2][1],"|",tablica[2][2],"")

def get_human_coordinates():

    move = input("Whats your next move? ").upper()
    if move == "QUIT":
        quit()
    while move not in 'A1,A2,A3,B1,B2,B3,C1,C2,C3'.split(","): #dodać drugi warunek:P
        print_board()
        move = input("Incorecct. Whats your next move? ").upper()
        if move == "QUIT":
            quit()
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
        if get_winning_player() != False:
            print("wygrał ",get_winning_player()[1])
            break
        if is_board_full(): 
            print("Tablica pełna koniec gry")
            break
        while X:
            holder = get_human_coordinates()
            if tablica[holder[0]][holder[1]] not in "X,O".split(","):
                implement_move(holder,"X")
                X= False
                break
            else:
                print("Wrong move, try again")
                print_board()
                
        else:
            holder = get_human_coordinates()
            if tablica[holder[0]][holder[1]] not in "X,O".split(","):
                implement_move(holder,"O")
                X= True
            else:
                print("Wrong move, try again")
                

def get_winning_player():
    
    # Checking for rows for win
    for row in range(0, 3):
        if tablica[row][0] == tablica[row][1] == tablica[row][2] and tablica[row][0] != '.':
            return True, tablica[row][0]
    
    # Checking for columns for win
    for col in range(0, 3):
        if tablica[0][col] == tablica[1][col] == tablica[2][col] and tablica[0][col] != '.':
            return True, tablica[0][col]
        
    # Checks for diagonals for win
    if tablica[0][0]==tablica[1][1]==tablica[2][2] and tablica[0][0]!='.':
        return True,tablica[0][0]
    if tablica[0][2]==tablica[1][1]==tablica[2][0] and tablica[0][2]!='.':
        return True,tablica[0][2]
    return False
    
def is_board_full():
    if not any("." in x for x in tablica): #nie wiem jak to działa 
        return True
    return False

def random_comp():
    x = []
    for row in range(0, 3):
        for col in range(0, 3):
            if tablica[row][col] == ".":
                x.append(str(row)+","+str(col))
                print(x)
    print(x[random.randrange(0,len(x))])
    return x[random.randrange(0,len(x))]   

def comp_lvl_begginer():
    X=True
    while True:
        print_board()

        if get_winning_player() != False:
            print("wygrał ",get_winning_player()[1])
            break
        if is_board_full(): 
            print("Tablica pełna koniec gry")
            break
        while X:
            holder = get_human_coordinates()
            if tablica[holder[0]][holder[1]] not in "X,O".split(","):
                implement_move(holder,"X")
                X= False
                break
            else:
                print("Wrong move, try again")
                print_board()
                
        else:
            holder = ([int(x) for x in random_comp().split(",")])
            implement_move(holder,"O")
            X= True
            
def unbeatable_ai():
    X=True
    i = 0
    while True:
        print_board()
        if is_board_full(): 
            print("Tablica pełna koniec gry")
            break
        if get_winning_player() != False:
            print("wygrał ",get_winning_player()[1])
            break
        while X:
            holder = get_human_coordinates()
            if tablica[holder[0]][holder[1]] not in "X,O".split(","):
                implement_move(holder,"X")
                X= False
                break
            else:
                print("Wrong move, try again")
                print_board()
        else:
            i += 1
            holder = get_unbeatable_ai_move(holder, i)
            time.sleep(1)
            implement_move(holder,"O")
            X= True            
            
def get_unbeatable_ai_move(human, i):
    # uznajac ze komputer zawsze gra jako O 
    if i == 1: # i == tura
        if human == [0,0] or human == [2,2] or human == [0,2] or human == [2,0]:
            return [1,1]
        elif human == [1,1]:
            return [2,2]
        elif human == [0,1] or human == [1,0] or human == [1,2] or human == [2,1]:
            return [1,1]
    if i == 2: # i == tura
        if tablica[1][1] == 'O': #trzeba dopisac wiecej if-ow czy jakies petle porobic
            if tablica[0][0] == 'X':
                if human == [0,1]:
                    return [0,2]
                elif human == [1,0]:
                    return [2,0]
                elif human == [0,2] or human == [1,2] or human == [2,2]:
                    return [0,1]
                elif human == [2,0] or human == [2,1]:
                    return [1,0]
            else:
                return checkBestMove_ai()
                
        if tablica[2][2] == 'O':
            if human == [1,2]:
                return [1,0]
            elif human == [0,2]:
                return [2,0]
            elif human == [0,1]:
                return [2,1]
            elif human == [0,0] or human == [2,0]:
                return [0,2]
            elif human == [1,0]:
                return [1,2]
            elif human == [2,1]:
                return [0,1]
        else:
            return checkBestMove_ai()
    
    if i == 3 or i == 4 or i == 5: #nie wiem jak bardzo potrzebne
        return checkBestMove_ai()
            
def checkBestMove_ai():
    #Checks for win/block condition and returns win or block move
    try:
        for row in range(0,3):
            if tablica[row][0] == '.': #Checks rows FIRST column for win or block
                if tablica[row][1] == tablica[row][2]:
                    return [row,0]
            if tablica[row][1] == '.': #Checks rows SECOND column for win or block
                if tablica[row][0] == tablica[row][2]:
                    return [row,1]
            if tablica[row][2] == '.': #Checks rows THIRD column for win or block
                if tablica[row][0] == tablica[row][1]:
                    return [row,2]
            

        for col in range(0,3):
            if tablica[0][col] == '.': #Checks columns FIRST row for win or block
                if tablica[1][col] == tablica[2][col]:
                    return [0,col]
            if tablica[1][col] == '.':
                if tablica[0][col] == tablica[2][col]:
                    return [1,col]
            if tablica[2][col] == '.': #Checks columns THIRD row for win or block
                if tablica[0][col] == tablica[1][col]:
                    return [2,col]

        #Checks for win diagonally
        if tablica[0][0]==tablica[1][1] and tablica[2][2] == '.':
            return [2,2]
        if tablica[1][1]==tablica[2][2] and tablica[0][0] == '.':
            return [0,0]
        if tablica[0][2]==tablica[1][1] and tablica[2][0] == '.':
            return [2,0]
        if tablica[1][1]==tablica[2][0] and tablica[0][2] == '.':
            return [0,2]
        if tablica[0][0]==tablica[2][2] or tablica[2][0]==tablica[0][2] and tablica[1][1] == '.':
            return [1,1]
    except:
        return [int(x) for x in random_comp().split(",")] #nie wiem jak to zrobic, aktualnie kiedy plansza jest juz nie do wygrania/blokowania wyskakuje blad. Probowalem losowy znak zeby dawalo zeby sie zapelnilo ale jest jakis bug :(

def main_menu():
    print("1) Zagraj z człowiekiem")
    print("2) Zagraj z komputerem (lvl. begginer)")
    print("3) Zagraj z komputerem (lvl. hard)")
    print("4) Wyjdź z gry")
    x= input("Podaj cyfrę od 1 do 4 ")
    if x == "1":
        onevone()
    if x == "2":
        comp_lvl_begginer()
        return
    if x == "3":
        unbeatable_ai()
        return
    if x == "4":
        quit()
    
while True:
    tablica = get_board()
    main_menu()
    

