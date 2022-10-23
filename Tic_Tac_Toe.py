def get_board():
    return [[ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ]]
                  #A              #B              #C
#print(get_board()[2][0])
                  #C#1 

def print_board():
    print("   1   2   3")
    print("A ",get_board()[0][0],"|",get_board()[0][1],"|",get_board()[0][2],"")
    print("  ---+---+---")
    print("A ",get_board()[1][0],"|",get_board()[1][1],"|",get_board()[1][2],"")
    print("  ---+---+---")
    print("A ",get_board()[2][0],"|",get_board()[2][1],"|",get_board()[2][2],"")

def get_human_coordinates():

    move = input("Whats your next move?")
    while move not in 'A1,A2,A3,B1,B2,B3,C1,C2,C3,a1,a2,a3,b1,b2,b3,c1,c2,c3'.split(","): #dodać drugi warunek:P
        move = input("Incorecct. Whats your next move?")
    if move[0] == 'A' or move[0] == 'a': #to głupie może jakoś zmienić?  
        if move[1] == '1':
            return "[0][0]"
        elif move[1] == '2':
            return "[0][1]"
        else:
            return "[0][3]"
    elif move[0] == 'B' or move[0] == 'b': #to głupie może jakoś zmienić?  
        if move[1] == '1':
            return "[1][0]"
        elif move[1] == '2':
            return "[1][1]"
        else:
            return "[1][3]"
    if move[0] == 'C' or move[0] == 'c': #to głupie może jakoś zmienić?  
        if move[1] == '1':
            return "[2][0]"
        elif move[1] == '2':
            return "[2][1]"
        else:
            return "[2][3]"


print(get_human_coordinates())
