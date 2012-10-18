from sys import exit
from random import randint

class Game(object):

    
    def __init__(self):
        pass

    def play(self):
        user_pt = 0
        cpu_pt = 0
        name = raw_input("Please enter your name: > ")
        print "Hello %s :) " % name
        print "************************\n"
        try:
            while True: 
                user_hand = self.next_round()
                point = self.check(user_hand)
                if point == 1:
                    user_pt += 1
                elif point == 2:
                    cpu_pt += 1
                else:
                    pass
                
        except EOFError:
            print "Endergebniss: %s %d CPU %d\n" % (name, user_pt, cpu_pt)
            if user_pt > cpu_pt:
                print "You won!! Good work"
            elif user_pt < cpu_pt:
                print "You lost! I'm sorry"
            else:
                print "Nobody has won! Try again!"
            print "\nBye"
        
    def check(self, user):
        cpu_hand = randint(1, 3)
        #print repr(cpu_hand)
        #print repr(user)
        schere = 1
        stein = 2
        papier = 3
        
        if user == cpu_hand:
            print "Nobody receives the point\n"
            return 0
            
        elif user == schere and cpu_hand == papier:
            print "You received the point\n"
            return 1
            
        elif user == papier and cpu_hand == stein:
            print "You received the point\n"
            return 1
            
        elif user == stein and cpu_hand == schere:
            print "You received the point\n"
            return 1

        else:
            print "The CPU receives a point\n"
            return 2
            
    def next_round(self):
        print "Please choose your hand: \n"
        print "1. Schere \n"
        print "2. Stein \n"
        print "3. Papier \n"
        print "(To quit press CTRL-D)"
        try:
            user_hand = int(raw_input("> "))
        except ValueError:
            print "This is not a number, please try again"
            self.next_round()
        return user_hand
            
a_game = Game()
a_game.play()
