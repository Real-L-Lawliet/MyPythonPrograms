import random
def menu():
    inp = int(input('\nEnter your Choice\n1 Rock \n2 Paper \n3 Scissors\n-> '))
    if inp == 1 or inp==2 or inp==3:
        return inp
    else:
        print('Invalid Choice')
        return None

cond = True
your_score = 0
pc_score = 0
    
while cond:
    inp = menu()
    pc = random.randint(1,3)
    
    
    if inp==1 and pc==2:
        print('\nYou: Rock\nPC: Paper\nComputer won the round')
        pc_score += 1

    elif inp==2 and pc==3:
        print('\nYou: Paper\nPC: Scissors\nComputer won the round')
        pc_score += 1
        
    elif inp==3 and pc==1:
        print('\nYou: Scissors\nPC: Rock\nComputer won the round')
        pc_score += 1
        
    elif pc==1 and inp==2:
        print('\nYou: Paper\nPC: Rock\nYou won the round')
        your_score += 1

    elif pc==2 and inp==3:
        print('\nYou: Scissors\nPC: Paper\nYou won the round')
        your_score += 1

    elif pc==3 and inp==1:
        print('\nYou: Rock\nPC: Scissors\nYou won the round')
        your_score += 1

    elif inp==None:
        continue
    
    else:
        print('\nDraw')
        your_score += 1
        pc_score += 1

    print('\n\nSCORE:\n--------------------------\nYou: ',your_score,'\nComputer: ',pc_score,'\n--------------------------')

    x = input('\nContinue the game?\n')
    if x=='No' or x=='no':
        cond = False
    
    
