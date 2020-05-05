"""
Implementing RPSLS for Practice Project
"""
import random
def name_to_number(name):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and returns integer (0-1-2-3-4)
    """
    if name=='rock':
        return 0
    elif name=='Spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4

def number_to_name(number):
    """
    Take an integer as input (0-1-2-3-4) 
    and returns string name (rock-Spock-paper-lizard-scissors)
    """
    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print("Enter number in range")
        
def rpsls(player_choice):
    """
    Takes player choice (rock-Spock-paper-lizard-scissors)
    and then returns the number (0-1-2-3-4) for the particular choice
    """
    
    if player_choice=='rock':
        player_number= name_to_number(player_choice)

    elif player_choice=='Spock':
        player_number= name_to_number(player_choice)
        
    elif player_choice=='paper':
        player_number= name_to_number(player_choice)
        
    elif player_choice=='lizard':
        player_number= name_to_number(player_choice)
        
    elif player_choice=='scissors':
        player_number= name_to_number(player_choice)
        
    else:
        print("Player's input is not correct")
        
    #generating random number for computer
    #then converting the number generated to the following name
    
    comp_number=(random.randrange(0,5))
    comp_choice= number_to_name(comp_number)
    
    #computing the diff between comp_number and player number
    #giving out only postive diff
    
    diff= (player_number-comp_number)%5
    
    #if the diff is 0 then it's a tie
    #if 1 or 2 then player wins
    #if it's 3 or 4 then computer wins
    
    if diff == 0:
        print(name,"chooses",player_choice)
        print("Computer chooses",comp_choice)
        print(name,"and computer tie!")
        print()
        
    elif diff == 1:
        print(name,"chooses",player_choice)
        print("Computer chooses",comp_choice)
        print(name," wins!")
        print()
        
    elif diff == 2:
        print(name,"chooses",player_choice)
        print("Computer chooses",comp_choice)
        print(name," wins!")
        print()
        
    else:
        print(name,"chooses",player_choice)
        print("Computer chooses",comp_choice)
        print("Computer wins!")
        print()
name=input("Your name:- ")
print(name,"chooses:-",end='')
choice=input()
print()
rpsls(choice)