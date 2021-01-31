import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from random import randint
from time import sleep
class player () : 
    def __init__(self): 
        self.moves=[] 
        self.choice=''
        self.status=False
        wining_moves=[]
    def set_choice(self,choice): 
        self.choice=choice
    def flatt_array(self):
        flat=[]
        for sublist in self.wining_moves:
            for item in sublist:
                flat.append(item)
        return(flat)

    def wins_by_colunm(self,dimension):
        moves=[]
        for i in range(1,dimension+1) :
            combo=[]
            for j in range(i,dimension**2+1,dimension) : 
                combo.append(j)
            moves.append(combo)
        return  moves


        
    def wins_by_row(self,dimension):
        moves=[]
        for i in range(1,dimension**2+1,dimension) :
            combo=[]
            for j in range(i,dimension+i) : 
                combo.append(j)
            moves.append(combo)
        return  moves

        
    def wins_by_diag(self,dimension):
        moves=[]
        combo=[]
        for i in range(1,dimension**2+1 ,dimension+1) :
            combo.append(i)
        moves.append(combo)
        
        combo=[]
        for i in range(dimension,(dimension**2+1)-(dimension-1) ,dimension-1) :
            combo.append(i)
        moves.append(combo)
        return moves
    
    def set_wining_moves(self,dimension) : 
        wining_moves_by_row=self.wins_by_row(dimension)
        wining_moves_by_colunm=self.wins_by_colunm(dimension)
        wining_moves_by_diag=self.wins_by_diag(dimension)
        self.wining_moves=[wining_moves_by_row,wining_moves_by_colunm,wining_moves_by_diag]
    
    
    def winner(self): 
        my_moves = self.moves 
        combos=self.flatt_array()
        winner=False
        for c in  combos :
            if winner == True :
                break 
            else : 
                winner = True 
                for element in c : 
                    if element not  in my_moves : 
                        winner = False
                        break  
        if winner : 
            self.status=True

    def play(self,Reserved_Moves,dimension) : 
        while True : 
        # the user will provide I,J of   the move 
            cprint('\nYour Turn Chose Position :)','yellow')
            choice=input('\n') 
            try : 
                choice=int(choice)
                # validate the I,J  
                if  choice>0 and choice <=  dimension**2 :  
                    if choice in Reserved_Moves : 
                          cprint('\nPosition is taken','yellow')
                    else : 
                        break
                else : 
                    # MUST BE IN THE MATRIX  #0<i,j<dimension
                    cprint('\nUnvalid Choice Please Chose  between {min} --- {max} \n'.format(min=1,max=dimension**2),'yellow')
            except : 
                cprint('Unvalid Choice Please Chose  between {min} --- {max} \n'.format(min=1,max=dimension**2),'yellow')
        self.moves.append(choice)
        if  len(self.moves) >=dimension:
            self.winner()
        return choice

    def play_Bot(self,Reserved_Moves,dimension) : 
        cprint('\nBot Turn  :)','yellow')
        sleep(1)
        while True : 
        # generate a random move  
                choice=randint(1, dimension**2)
                if choice not in Reserved_Moves : 
                    break 
        self.moves.append(choice)
        if  len(self.moves) >=dimension:
            self.winner()
        return choice
