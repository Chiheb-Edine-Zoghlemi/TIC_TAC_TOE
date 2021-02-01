from player import player
import numpy as np 
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) 
from termcolor import cprint 
from pyfiglet import figlet_format


def Winner_Exist(p1,p2,bot):
    if p1.status == True : 
        cprint('\nPlayer  1  Wins \n','green')
        return True 
    elif p2.status == True : 
        if bot :
            cprint('\n BOT Wins \n ','green')
        else : 
            cprint('\n Player 2 Wins \n ','green')
        return True
    else : 
        return False

#for responsuve  display 
def creat_line(dimension):
    line='\n'
    for i in range(dimension) : 
        line  = line+'-------'
    line=line+'\n'
    return line

#for displaying the matrix 
def display_matrix(matrix,dimension) : 
    line=creat_line(dimension)
    ch=line
    for i in  range(dimension):
        for j  in range(dimension) : 
            index=matrix[i][j]
            if type(index) == int :
                if index < 10 :
                    ch=ch+("|  {index}  |".format(index=index))
                elif index<100 : 
                    ch=ch+("|  {index} |".format(index=index))
                else : 
                    ch=ch+("| {index} |".format(index=index))
            else : 
                ch=ch+("|  {index}  |".format(index=index))

        ch=ch+line
    print(ch)

# display the copyright section when the program exist      
def exit_program() : 
    cprint('\n===============================================================','blue')
    cprint('Developped By : Chiheb Edine Zoghlemi & Malek Hammou','red')
    print('Contact Links -->   Chiheb Edine Zoghlemi')
    print('Linkdin => https://www.linkedin.com/in/chihebedinezoghlemi/ ')
    print('Github => https://github.com/Chiheb-Edine-Zoghlemi ')
    print('Contact Links -->   Malek Hammou')
    print('Linkdin => https://www.linkedin.com/in/malekhammou/ ')
    print('Github => https://github.com/malekhammou ')
    cprint('===============================================================','blue')
    
# this function interact with the user to create the matrix it returns matrix,dimension
def set_matrix() : 
    cprint('Please chose the matrix dimension \n','yellow')
    while True : 
        try : 
            dimension=int(input())
            if dimension > 0 : 
                break 
            else : 
                cprint('Please chose the matrix dimension \n','yellow')
        except : 
            cprint('Please chose the matrix dimension \n','yellow')
       
    matrix = [ [ 0 for i in range(dimension) ] for j in range(dimension) ]
    index=1
    for i in range(dimension):
        for j in range(dimension) : 
            matrix[i][j]=index
            index=index+1
    display_matrix(matrix,dimension)
    return dimension,matrix
#set the player // return a player 
def set_Bot(dimension) : 
    p=player()
    p.set_wining_moves(dimension)
    while True : 
        cprint('Chose BOT Symbole \n ','yellow')
        symbole=input('\n')
        try :
            symbole=int(symbole)
        except : 
            p.set_choice(choice=symbole)
            break 
    return  p
#set the player // return a player 
def set_player(dimension,i) : 
    p=player()
    p.set_wining_moves(dimension)
    while True : 
        cprint('Player {i} Chose Your Symbole \n '.format(i=i),'yellow')
        symbole=input('\n')
        try :
            symbole=int(symbole)
        except : 
            p.set_choice(choice=symbole)
            break 
    return  p

def menu () : 
            cprint('\n===============================================================','blue')
            cprint('                              Game Menu','red')
            cprint('===============================================================','blue')
            print('2 Player Mode              || Press 1 ')
            print('Player VS Bot              || Press 2 ')
            print('To change matrix dimension || Press 3 ')
            print('To Exit                    || Press + ')
            
            
            #verify the user choice
            while True :
                #get the user choice 
                choice=input('\n')
                try : 
                    choice = int(choice)
                    if choice == 1 or choice == 2  or choice == 3: 
                        break
                    else : 
                        cprint('Please  provide a valid choice ','yellow')
                except : 
                    if  choice == '+' : 
                        break 
                    else :
                        cprint('Please  provide a valid choice ','yellow')
            return choice
#the game  fot vs bot 
def vsbot_game(p1,p2,matrix,dimension):
    Reserved_Moves=[]
    for role in range(dimension**2) :
        if Winner_Exist(p1,p2,True): 
            display_matrix(matrix,dimension)
            break 
        elif role % 2 == 0 : 
            
            display_matrix(matrix,dimension)
            choice=p1.play(Reserved_Moves,dimension)
            postion=[(index, row.index(choice)) for index, row in enumerate(matrix) if choice in row]
            postion=postion[0]
            matrix[postion[0]][postion[1]] = p1.choice
            Reserved_Moves.append(choice)
        else : 
            
            display_matrix(matrix,dimension)
            choice=p2.play_Bot(Reserved_Moves,dimension)
            postion=[(index, row.index(choice)) for index, row in enumerate(matrix) if choice in row]
            postion=postion[0]
            matrix[postion[0]][postion[1]] = p2.choice
            Reserved_Moves.append(choice)
    if role == dimension**2 : 
        cprint('---- DRAW ----','yellow')


#the game for 2 players 
def twoplayer_game(p1,p2,matrix,dimension):
    Reserved_Moves=[]
    for role in range(dimension**2) :
        if Winner_Exist(p1,p2,False): 
            display_matrix(matrix,dimension)
            break 
        elif role % 2 == 0 : 
            cprint('\nPLAYER 1 ','yellow')
            display_matrix(matrix,dimension)
            choice=p1.play(Reserved_Moves,dimension)
            postion=[(index, row.index(choice)) for index, row in enumerate(matrix) if choice in row]
            postion=postion[0]
            matrix[postion[0]][postion[1]] = p1.choice
            Reserved_Moves.append(choice)
        else : 
            cprint('\nPLAYER 2 ','yellow')
            display_matrix(matrix,dimension)
            choice=p2.play(Reserved_Moves,dimension)
            postion=[(index, row.index(choice)) for index, row in enumerate(matrix) if choice in row]
            postion=postion[0]
            matrix[postion[0]][postion[1]] = p2.choice
            Reserved_Moves.append(choice)
    if role == dimension**2 : 
        cprint('---- DRAW ----','yellow')
#in case he chose the 2 player mode 
def twoplayers(matrix,dimension):
    cprint('\n===============================================================','blue')
    cprint('                         2 PLAYERS MODE','red')
    cprint('===============================================================','blue')
    p1=set_player(dimension,1)
    p2=set_player(dimension,2)
    twoplayer_game(p1,p2,matrix,dimension)

# in case he chose the vs bot mode 
def vsbot(matrix,dimension):
    cprint('\n===============================================================','blue')
    cprint('                         VS BOT MODE','red')
    cprint('===============================================================','blue')
    display_matrix(matrix,dimension)
    p1=set_player(dimension,1)
    p2=set_Bot(dimension)
    vsbot_game(p1,p2,matrix,dimension)

#switch case implemented in python 
def Switcher(i,matrix,dimension):
        switcher={
                1:twoplayers,
                2:vsbot
                }
        func=switcher.get(i,lambda :'Invalid Choice')
        func(matrix,dimension) 
#main section 
def main() : 
    cprint(figlet_format('TIC', font='broadway'),'green', attrs=['bold'])
    cprint(figlet_format('TAC', font='broadway'),'green', attrs=['bold'])
    cprint(figlet_format('TOE', font='broadway'),'green', attrs=['bold'])
    
    cprint('                      Setting Board Dimension','red')
    cprint('===============================================================\n','blue')
    while True :
        dimension,matrix=set_matrix()
        choice = menu()
        if choice == '+' : 
            exit_program()
            break 
        elif choice==3 : 
            dimension,matrix=set_matrix()
        else : 
            Switcher(choice,matrix,dimension)





if __name__ == '__main__' : 
    main()