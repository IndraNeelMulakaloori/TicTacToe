#This program(game) is coded in a simple way without any advanced algortihms in OOPS paradigm
import time
import sys
#Defining a Board class
class Board():
    def __init__(self):
        '''
        Args: instance 
        The init method intialses and stores the coordinates of the player in a nested list = cells
        '''
        self.cells =[['','',''],['','',''],['','','']]

    def display(self):
        '''
        Args : the instance self
        Returns : None
        The diplay method prints the current 'X' and 'O' positions from the cells
        '''
        print(f"  {self.cells[0][0]} |  {self.cells[0][1]} |  {self.cells[0][2]}")
        print("------------")
        print(f"  {self.cells[1][0]} |  {self.cells[1][1]} |  {self.cells[1][2]}")
        print("------------")
        print(f"  {self.cells[2][0]} |  {self.cells[2][1]} |  {self.cells[2][2]}")
        time.sleep(1.5)
    
    def update_cells(self,p,x,y):
        '''
        Args : p = player,str
               x , y = coordiantes of the move (int,int)
        Returns : None
        It updates the current move of the player
        '''
        x = x-1
        y = y-1
        if self.cells[x][y] == '':
          self.cells[x][y] =  p
                 

    def decison(self,player):
        '''
        Args : player,str
        Returns : returns True if any of the function is True 
        '''
        if ((self.cells[0][0] == player and self.cells[0][1] == player and self.cells[0][2] == player) or 
           (self.cells[1][0] == player and self.cells[1][1] == player and self.cells[1][2] == player) or  
           (self.cells[2][0] == player and self.cells[2][1] == player and self.cells[2][2] == player) or
           #Column check
           (self.cells[0][0] == player and self.cells[1][0] == player and self.cells[2][0] == player) or
           (self.cells[0][1] == player and self.cells[1][1] == player and self.cells[2][1] == player) or
           (self.cells[0][2] == player and self.cells[1][2] == player and self.cells[2][2] == player) or
           #Diagonal Check
           (self.cells[0][0] == player and self.cells[1][1] == player and self.cells[2][2] == player) or
           (self.cells[2][0] == player and self.cells[1][1] == player and self.cells[0][2] == player)) :
              print(f"Player {player} won the game")
              return True 

        
        else:
            # If the above conditon isn't True ,then the game maybe a tie.
            used_cells = 0
            for i in self.cells :
                for c in i:
                    if c != '':
                        used_cells+=1
            
            if used_cells == 9:
                print("\nIt's a draw\n")
                return True 
        return False


class Bot():
      """
      The Bot class is a pre programmed player which is used play against a human player
      """
      def bot_moves(self,p):
       """
       Args : p (str)
       Return : Start move,Winning moves or block moves are confined in a bot_moves method,
       """
        #Start move
       if b.cells[1][1] == '':
           b.cells[1][1] = p
           return
           
        
       #Winning moves
       if self.across_bot_moves(p) == True:
           b.decison(p)
           return
       
       if self.vertical_bot_moves(p) == True:
           b.decison(p)
           return

       if self.diagonal_bot_moves(p) == True:
           b.decison(p)
           return
       
       #Blockmoves
       if (b.cells[0][0] != p and b.cells[0][0] != '' ) and (b.cells[0][1]!= p and b.cells [0][1] != '') and b.cells[0][2] == '':
           b.cells[0][2] = p
           return 
       
       if (b.cells[0][0] != p and b.cells[0][0] != '' ) and (b.cells[0][2]!= p and b.cells [0][2] != '') and b.cells[0][1] == '':
           b.cells[0][1] = p
           return 

       if (b.cells[0][1] != p and b.cells[0][1] != '' ) and (b.cells[0][2]!= p and b.cells [0][2] != '') and b.cells[0][0] == '':
           b.cells[0][0] = p
           return 

       if (b.cells[1][0] != p and b.cells[1][0] != '' ) and (b.cells[1][1]!= p and b.cells [1][1] != '') and b.cells[1][2] == '':
           b.cells[1][2] = p
           return 
       
       if (b.cells[1][0] != p and b.cells[1][0] != '' ) and (b.cells[1][2]!= p and b.cells [1][2] != '') and b.cells[1][1] == '':
           b.cells[1][1] = p
           return 

       if (b.cells[1][1] != p and b.cells[1][1] != '' ) and (b.cells[1][2]!= p and b.cells [1][2] != '') and b.cells[1][0] == '':
           b.cells[1][0] = p
           return 
       
       if (b.cells[2][0] != p and b.cells[2][0] != '' ) and (b.cells[2][1]!= p and b.cells [2][1] != '') and b.cells[2][2] == '':
           b.cells[2][2] = p
           return 

       if (b.cells[2][0] != p and b.cells[2][0] != '' ) and (b.cells[2][2]!= p and b.cells [2][2] != '') and b.cells[2][1] == '':
           b.cells[2][1] = p
           return 

       if (b.cells[2][1] != p and b.cells[2][1] != '' ) and (b.cells[2][2]!= p and b.cells [2][2] != '') and b.cells[2][0] == '':
           b.cells[2][0] = p
           return 
        
       if (b.cells[0][0] != p and b.cells[0][0] != '' ) and (b.cells[1][0]!= p and b.cells [1][0] != '') and b.cells[2][0] == '':
           b.cells[2][0] = p
           return 
       
       if (b.cells[0][0] != p and b.cells[0][0] != '' ) and (b.cells[2][0]!= p and b.cells [2][0] != '') and b.cells[1][0] == '':
           b.cells[1][0] = p
           return 
        
       if (b.cells[1][0] != p and b.cells[1][0] != '' ) and (b.cells[2][0]!= p and b.cells [2][0] != '') and b.cells[0][0] == '':
           b.cells[0][0] = p
           return 
       
       if (b.cells[0][1] != p and b.cells[0][1] != '' ) and (b.cells[1][1]!= p and b.cells [1][1] != '') and b.cells[2][1] == '':
           b.cells[2][1] = p
           return 

       if (b.cells[0][1] != p and b.cells[0][1] != '' ) and (b.cells[2][1]!= p and b.cells [2][1] != '') and b.cells[1][1] == '':
           b.cells[1][1] = p
           return 
       
       if (b.cells[1][1] != p and b.cells[1][1] != '' ) and (b.cells[2][1]!= p and b.cells [2][1] != '') and b.cells[0][1] == '':
           b.cells[0][1] = p
           return 
       
       if (b.cells[0][2] != p and b.cells[0][2] != '' ) and (b.cells[1][2]!= p and b.cells [1][2] != '') and b.cells[2][2] == '':
           b.cells[2][2] = p
           return 

       if (b.cells[0][2] != p and b.cells[0][2] != '' ) and (b.cells[2][2]!= p and b.cells [2][2] != '') and b.cells[1][2] == '':
           b.cells[1][2] = p
           return 

       if (b.cells[1][2] != p and b.cells[1][2] != '' ) and (b.cells[2][2]!= p and b.cells [2][2] != '') and b.cells[0][2] == '':
           b.cells[0][2] = p
           return 
      
       if (b.cells[0][0] != p and b.cells[0][0] != '' ) and (b.cells[1][1]!= p and b.cells [1][1] != '') and b.cells[2][2] == '':
           b.cells[2][2] = p
           return  
       
       if (b.cells[0][0] != p and b.cells[0][0] != '' ) and (b.cells[2][2]!= p and b.cells [2][2] != '') and b.cells[1][1] == '':
           b.cells[1][1] = p
           return 
        
       if (b.cells[1][1] != p and b.cells[1][1] != '' ) and (b.cells[2][2]!= p and b.cells [2][2] != '') and b.cells[0][0] == '':
           b.cells[0][0] = p
           return 
       
       if (b.cells[0][2] != p and b.cells[0][2] != '' ) and (b.cells[1][1]!= p and b.cells [1][1] != '') and b.cells[2][0] == '':
           b.cells[2][0] = p
           return 
       
       if (b.cells[0][2] != p and b.cells[0][2] != '' ) and (b.cells[2][0]!= p and b.cells [2][0] != '') and b.cells[1][1] == '':
           b.cells[1][1] = p
           return 
      
       if (b.cells[1][1] != p and b.cells[1][1] != '' ) and (b.cells[2][0]!= p and b.cells [2][0] != '') and b.cells[0][2] == '':
           b.cells[0][2] = p
           return 


       
       else:
            for i in range(0,3):
                for j in range(0,3):
                    if b.cells[i][j] == '':
                        b.cells[i][j] = p
                        return
       
      def across_bot_moves(self,p):
        if b.cells[0][0] == p and b.cells[0][1] == p and b.cells[0][2] == '':
           b.cells[0][2] = p
           return True
       
        if b.cells[1][0] == p and b.cells[1][1] == p and b.cells[1][2] == '':
           b.cells[1][2] = p
           return True
        
        if b.cells[2][0] == p and b.cells[2][1] == p and b.cells[2][2] == '':
           b.cells[2][2] = p
           return True
       
        if b.cells[0][0] == '' and b.cells[0][1] == p and b.cells[1][2] == p:
           b.cells[0][0] = p
           return True

        if b.cells[1][0] == '' and b.cells[1][1] == p and b.cells[1][2] == p:
           b.cells[1][0] = p
           return True

        if b.cells[2][0] == '' and b.cells[2][1] == p and b.cells[2][2] == p:
           b.cells[2][0] = p
           return True

        if b.cells[0][0] == p and b.cells[0][1] == '' and b.cells[0][2] == p:
           b.cells[0][1] = p
           return True
        
        if b.cells[1][0] == p and b.cells[1][1] == '' and b.cells[1][2] == p:
           b.cells[1][1] = p
           return True

        if b.cells[2][0] == p and b.cells[2][1] == '' and b.cells[2][2] == p:
           b.cells[2][1] = p
           return True

        return False
      def vertical_bot_moves(self,p):
        if b.cells[0][0] == p and b.cells[1][0] == p and b.cells[2][0] == '':
           b.cells[2][0] = p
           return True
       
        if b.cells[0][1] == p and b.cells[1][1] == p and b.cells[2][1] == '':
           b.cells[2][1] = p
           return True
        
        if b.cells[0][2] == p and b.cells[1][2] == p and b.cells[2][2] == '':
           b.cells[2][2] = p
           return True
       
        if b.cells[0][0] == '' and b.cells[1][0] == p and b.cells[2][0] == p :
           b.cells[0][0] = p
           return True

        if b.cells[0][1] == '' and b.cells[1][1] == p and b.cells[2][1] == p:
           b.cells[0][1] = p
           return True

        if b.cells[0][2] == '' and b.cells[1][2] == p and b.cells[2][2] == p:
           b.cells[0][2] = p
           return True

        if b.cells[0][0] == p and b.cells[1][0] == '' and b.cells[2][0] == p:
           b.cells[1][0] = p
           return True
        
        if b.cells[0][1] == p and b.cells[1][1] == '' and b.cells[2][1] == p:
           b.cells[1][1] = p
           return True

        if b.cells[0][2] == p and b.cells[1][2] == '' and b.cells[2][2] == p:
           b.cells[1][2] = p
           return True

        return False
      def diagonal_bot_moves(self,p):
        if b.cells[0][0] == p and b.cells[1][1] == p and b.cells[2][2] == '':
            b.cells[2][2] = p   
            return True

        if b.cells[0][0] == p and b.cells[1][1] == '' and b.cells[2][2] == p:
            b.cells[1][1] = p  
            return True
        
        if b.cells[0][0] == '' and b.cells[1][1] == p and b.cells[2][2] == p:
            b.cells[0][0] = p  
            return True
        if b.cells[0][2] == p and b.cells[1][1] == p and b.cells[2][0] == '':
            b.cells[2][0] = p  
            return True

        if b.cells[0][2] == p and b.cells[1][1] == '' and b.cells[2][0] == p:
            b.cells[1][1] = p  
            return True
        
        if b.cells[0][2] == '' and b.cells[1][1] == p and b.cells[2][0] == p:
            b.cells[0][2] = p   
            return True
        
        return False
 
class Gameplay():
     """
     The class Gameplay is created which contains all the player decisons and gameplay loops(methods) 
     """

     def playergameplay(self,p1,p2):
         """
         The player vs player gameplay is programmed in this loop
         Args : p1,p2-str
         Returns : None
         """
         while True:
                print(f"\n It's player 1 {p1} turn  \n")
                x,y = [int(x) for x in input("Enter The move(i.e row(1,3),column number(1,3)with a space): ").split()] 
                b.update_cells (p1 , x , y)
                b.display()

                if b.decison(p1) ==True:
                    time.sleep(4)
                    break
                


                print(f"\n It's player 2  {p2} turn  \n")
                c,d = [int(x) for x in input("\nEnter The move(i.e row(1,3),column number(1,3) with a space):").split()]
                b.update_cells(p2,c,d)
                b.display()

                if b.decison(p2) == True:
                    time.sleep(4)
                    break    
                
    
     def bot_gameplay(self,p1,p2):
         '''
            The player vs bot gameplay is programmed and execued in th following while loop.
            Args : p1,p2-str
            Returns : None
         '''
         while True:
            print(f"\n It's player 1 {p1} turn  \n")
            x,y = [int(x) for x in input("Enter The move(i.e row,column number with a space): ").split()] 
            b.update_cells(p1,x,y)
            b.display()

            if b.decison(p1) ==True:
               time.sleep(4)
               break
            
            be.bot_moves(p2)
            b.display()
            if b.decison(p2) ==True:
               time.sleep(4)
               break
     
            
        
        
     def Intro(self): 
        '''
         Args : None 
         Returns : None
         The whole decison of player's choice i.e(selecting the mode and the player's symbol) is programmed in this block.
        ''' 
        try:
            print("\n1.Player Vs Player 2.Player VS BOT\n ")
            x = int(input("Enter your number Here -> "))
            if x!=1 and x!=2:
                raise print("Invalid number")
            print("Enter choice of player \n 1.X   2.O")
            p1 = int(input("Enter 1 or 2 Here -> ")) 
            if p1 != 1 and p1 != 2:
                raise print("Invalid number")
            if  p1 == 1:
                    p1 = 'X'
                    p2 = 'O'
            else:
                p1 = 'O'
                p2 = 'X'
            
            if x == 1:
                g.playergameplay(p1,p2)
            if x == 2:  
                g.bot_gameplay(p1,p2)
        
        except:
            print("Exit and try again for another game")
            
        
            
            

b = Board()
be = Bot()
g = Gameplay()
def print_header():
    '''
    Args : None
    Returns : None
    Prints the Title
    '''
    print("\nWelcome to Tic Tac Toe \n")



def main():
    '''
    This is the main function which exceutes the whole code
    '''
    print_header()
    b.display()  #Printing the header
    g.Intro()

main() 
        

    



    
    

        
         
