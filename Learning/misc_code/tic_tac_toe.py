def display_board(board):
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    
def player1_name():
    return input('Enter Player1 name: ')
    
def player2_name():
    return input('Enter Player2 name: ')
    
def check_board_full(board):
    board_full= all([x!=' ' for x in board])
    if board_full==True:
        return True
    else:
        return False
    # OR (list_full = not any([x==' ' for x in list1])  )      
    
def position_user1(player1):
    
    choice = 'WRONG'
    acceptable_range=['0','1','2','3','4','5','6','7','8']
    while choice not in acceptable_range or choice.isdigit()==False or board[int(choice)] != ' ':
        
        choice=input(f'{player1} pick a position: ')
        
        if choice not in acceptable_range or choice.isdigit()==False:
            print('Sorry, Invalid choice!')
        elif board[int(choice)] != ' ':
            print('Sorry, this position is already filled!')   
        
            
    return int(choice)

def position_user2(player2):
    
    choice='WRONG'
    acceptable_range=['0','1','2','3','4','5','6','7','8']
    while choice not in acceptable_range or choice.isdigit()==False or board[int(choice)] != ' ':
        
        choice=input(f'{player2} pick a position: ')
        
        if choice not in acceptable_range or choice.isdigit()==False:
            print('Sorry, Invalid choice!')
            
        elif board[int(choice)] != ' ':
            print('Sorry, this position is already filled!')
            
    return int(choice)

def user1_replacement(board,position):
    
    replacement='X'
    
    board[position]=replacement
    return board

def check_player1_won(player1):
    player1_won=False
    winning_combos = [(0,1,2), (0,4,8), (0,3,6), (1,4,7), (2,5,8), (2,4,6), (3,4,5), (6,7,8)]
    if any([board[combo[0]] == board[combo[1]] == board[combo[2]] == 'X' for combo in winning_combos]): 
        display_board(board)
        print(f'Congratulations! {player1} wins.')
        return True
    else:
        return player1_won
    
def user2_replacement(board,position):
    
    replacement='O'
    
    board[position]=replacement
    return board

def check_player2_won(player2):
    player2_won=False
    winning_combos = [(0,1,2), (0,4,8), (0,3,6), (1,4,7), (2,5,8), (2,4,6), (3,4,5), (6,7,8)]
    if any([board[combo[0]] == board[combo[1]] == board[combo[2]] == 'O' for combo in winning_combos]):  
        display_board(board)
        print(f'Congratulations! {player2} wins.' )
        return True
    else:
        return player2_won
    
#from IPython.display import display
game_on=True

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

player1 = player1_name()
          
player2 = player2_name()
    

while game_on:
    
    display_board(board)
    
    position= position_user1(player1)
    
    board = user1_replacement(board,position)
    
    player1_won= check_player1_won(player1)
    if player1_won == True:
        game_on=False
        break
                    
    else:
        display_board(board)
        
    board_full=check_board_full(board)
    
    if board_full==False:
        
        position = position_user2(player2)

        board = user2_replacement(board,position)
    
        player2_won= check_player2_won(player2)
            
        if  player2_won == True:
            game_on=False
            break
        else:
            
            continue
            
    else:
            
        print('MATCH DRAWN')
        game_on=False
    