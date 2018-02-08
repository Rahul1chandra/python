import random

def guess_No_game():
    gen_random = random.randrange(1,10)
    chance = 3
    #print ("generated no is ::",gen_random)
    while(chance != 0):
        urno = int(input("enter no"))
        if urno == gen_random:
            print ("congrats u won")
            return
        elif(urno > gen_random):
            print ("required no is lesser than ", urno)
        elif(urno < gen_random):
            print ("required no os greater than ", urno)
        else:
            print ("Invalid no:")
        chance = chance - 1    
        print ("ur change remaining",chance)
    if chance == 0:
        print ("game over!!")        
if __name__ == "__main__":
    guess_No_game()