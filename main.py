import random

user_win = 0
computer_win = 0

ans = ['rock','paper','scissor']     #keeping given option in a list
#index->  0      1        2
#rock vs paper -> paper wins
#rock vs scissor -> scissor wins
#paper vs scissor -> scissor wins

name = input("Please Enter Your Name: ")
while True:
    user_pick = (input('''
        Game Starts.....
    
        Rock
        Paper 
        Scissor 
        Q to Quit and Display Score
    
        ''')).lower()    #change all the input to lower case
    if user_pick == 'q':
        break
    if user_pick not in ans:
        print("Please enter within given options......")
        continue
    
    
    random_number = random.randint(0,2)
    computer_pick = ans[random_number]
    print(f'''
        Computer has picked {computer_pick}. 
        {name} Picked {user_pick}.
        ''')
    
    
    if user_pick == 'rock'  and  computer_pick == 'scissor':
        print(f'{name} Won....')
        user_win += 1
    
    elif user_pick == 'paper'  and computer_pick == 'rock':
        print(f'{name} Won.....')
        user_win += 1
    
    
    elif user_pick == 'scissor'  and computer_pick == 'paper':
        print(f'''
            {name} Won....
            ''')
        user_win += 1
    
    elif user_pick == computer_pick:
        print('''
            Same Choice.....
            ''')
        
    
    else:
        print(f'''
        {name} Lost..... 
        Computer Won....
        ''')
        computer_win += 1


if(user_win>computer_win):
    print(f'''
            Congratulations {name} Won!!!
        {name} Score : {user_win}
        Computer Score : {computer_win}
        ''')
    
elif(user_win == computer_win):
    print(f'''
        Its a Draw
        Computer Score : {computer_win}
        {name} Score : {user_win}
        ''')

else:
    print(f'''
        Computer Won!!!
        {name} Score : {user_win}
        Computer Score : {computer_win}.
        ''')
    
print(f'''
        GoodBye......
        Thanks {name} for Playing
    ''')