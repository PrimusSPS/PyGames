# TIC TAC TOE
# LET THE GAME BEGIN

#Function Block
from IPython.display import clear_output
# To check for winner
def check(mylist):
    
    # Horizontal Check
    n1=0 
    n2=3
    while n2<=9:
        if mylist[n1:n2]==['O','O','O'] or mylist[n1:n2]==['X','X','X']:
            return mylist[n1:n2]
        n1+=3
        n2+=3 
    
    # Verticle Check    
    n1=0 
    while n1<=2:
        if mylist[n1:9:3]==['O','O','O'] or mylist[n1:9:3]==['X','X','X']:
            return mylist[n1:9:3]
        n1+=1
        
    # Diagnal Check 
    if mylist[:9:4]==['X','X','X'] or mylist[:9:4]==['O','O','O']:
        return mylist[:9:4]
       
    if mylist[2:7:2]==['X','X','X'] or mylist[2:7:2]==['O','O','O'] :
        return mylist[2:7:2]
   
    # When all conditions above fail. Match Ties
    return 'Tie'

# To Print Board
def show_board(grid):
    print(f'   {grid[0]}  |  {grid[1]}  | {grid[2]}   ')
    print('  ____|_____|____')
    print(f'   {grid[3]}  |  {grid[4]}  | {grid[5]}   ')
    print('  ____|_____|____')
    print(f'   {grid[6]}  |  {grid[7]}  | {grid[8]}   ')
    print('      |     |    ')
           
# Rematch
def rematch():
    print('\n Press 1 for rematch and 2 for exit')
    command=input('\n Input the command: ')
    return command
    
# Main Block          
print(" TiC-TaC-ToE v1.0 ")
print('\n This is a Tic-Tac-Toe game.\n Player 1 --> 0 \n Player 2 --> X')
print('\n 1) Start Game \n 2) Exit')

start=input('\n Input the command: ')
while start=='1':
    board=[1,2,3,4,5,6,7,8,9]
    print('\n The Game has Started. Player 1 will have the first move. ')
    num=0
    while num<9:
                
        # Fn to print board
        clear_output()
        show_board(board)
        print(' Input the number from the board where you want to input')        
        
        # Assigning player numbers to alternate indexs
        if num%2==0:
            player = '1'
        else:
            player = '2'
        
        turn=int(input(f" Player {player}'s Move: "))
        
       # Appling inputted moves
        if player == '1':
            board[turn-1]='O'
        else:
            board[turn-1]='X'
        
        # checking for result 
        if num>=4:
            winner=check(board)
            # WINNER
            if   winner == ['O','O','O']:
                clear_output()
                show_board(board)
                print('\n Player 1 won the game. ')
                start=rematch() 

            elif winner == ['X','X','X']:
                clear_output()
                show_board(board)
                print('\n Player 2 won the game. ')
                start=rematch() 

            elif winner == 'Tie' and num==8:     
                clear_output() 
                show_board(board)
                print("\n Match Tied.") 
                start=rematch() 
        num+=1
else:
    exit()