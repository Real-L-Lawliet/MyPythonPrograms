from random import randint


class Player:
    def __init__ (self,name):
        self.name = name
        self.dice = 0

    def play(self,b):
        self.a = a
        self.b = b
        play = input('Enter Yes to Play\n')
        while play:
            Dice_of_A = randint(1,6)
            Dice_of_B = randint(1,6)
            print(self.name,': ',Dice_of_A,b,': ',Dice_of_B)
            if Dice_of_A >Dice_of_B:
                print( self.name,'wins')
            elif Dice_of_A==Dice_of_B:
                print('Draw')
            else:
                print(b,'wins')
            play = input('\nContinue Playing\n')
            if play=='No' or play=='no':
                play = False
        

a = Player('Justin')
b = Player('Sue')


a.play(b.name)
