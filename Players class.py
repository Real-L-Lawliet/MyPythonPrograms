from random import randint


class Players:
    def __init__ (self,name1,name2):
        self.name1 = name1
        self.name2 = name2
        self.score1 = 0
        self.score2 = 0

    def roll(self):
        play = input('Enter Yes to Play\n')
        turn = 0
        while play:
            turn+=1
            a = randint(1,6)
            b = randint(1,6)
            self.score1 += a
            self.score2 += b
            print('\n------------------------------------------------------------------------------\nTurn: ',turn)
            print('Dice value for',self.name1,':',a,'\nDice Value for',self.name2,':',b)
            print('\n-----------------------------\nTotal Score:\n',self.name1,':',self.score1,'    ',self.name2,':',self.score2,'\n-----------------------------')
            if self.score1 > self.score2:
                print( self.name1,'is ahead')
            elif self.score1==self.score2:
                print('Both are at same postion')
            else:
                print(self.name2,'is ahead')
            play = input('\nRoll Again?\n')
            if play=='No' or play=='no':
                play = False
            print('-----------------------------')
a = input('Enter the name of the 1st Player--> ')
b = input('Enter the name of the 2nd Player--> ')
Ludo = Players(a,b)


Ludo.roll()
