#BlackedJack v1.0

# Importing Libraries
from IPython.display import clear_output
from random import shuffle
from random import randint

#Golbal Elite
total_money=100
suit=['♠️','♣️','♥️','♦️']
face=['Two','Three','Four','Fives','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
rank={'Two':2,'Three':3,'Four':4,'Fives':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

# Class and Function Definitions

# Gives fresh shuffled deck
class Deck:
    
    def __init__(self):
        self.mydeck=[]
        for num1 in suit:
            for num2 in face:
                (self.mydeck).append((num1,num2))
        shuffle(self.mydeck)

# Gives random card from the deck    
class DrawCard:
    
    def __init__(self,usedeck):
        randomindex = randint(0,len(usedeck.mydeck)-1)
        self.mycard = usedeck.mydeck[randomindex]
        (usedeck.mydeck).pop(randomindex)
        
    def __str__(self):
        return f'{self.mycard[0]} {self.mycard[1]} {self.mycard[0]}'

# Betting Function              
def betting():
    chip=int(input("Input the Betting Amount: ₹"))
    if chip > total_money:
        print("You can't bet more than total money in your Wallet. Try again.")
        chip=betting()

    return chip    

# Prints cards in the hand 
def showhand(cardlist):
    i=0
    while i<len(cardlist):
        print(f'{cardlist[i][0]} {cardlist[i][1]} {cardlist[i][0]}',end=' ')
        i+=1
    print("\n")    
    
# Initialising Game with basic rules    
def Deal():
    for num in [1,2,3,4]:
        getcard=DrawCard(getdeck)
        if num in [1,2]:
            userhand.append(getcard.mycard)
            if num==1:
                print("\n User's Hand")
            print(getcard)
        else:    
            cpuhand.append(getcard.mycard)
            if num==3:
                print("\n Dealer's Hand")
                print(getcard)
            else:
                print('* Hidden *')

# Asks user for Hit or Stand after Deal                
def user_choice():
    
    while True:
        print("\n 1)  Hit --> Take Another Card from Deck")
        print(" 2) Stand--> Keep the given Hand")
        choice=input(" Input your Choice:")
        if choice == '1':
            go=double_jack()
            if go==True:
                getcard=DrawCard(getdeck)
                userhand.append(getcard.mycard)
                print("\n Your Hand--> ") 
                showhand(userhand)
                go=double_jack()
                if go==False:
                	return go
            else:
                return False
            
        else:
            print(" Your Hand Standed \n Your Hand--> ")
            showhand(userhand)
            return True

# Returns score/sum of cards in given hand    
def handsum(hand):
    sum=0
    for num in hand:
        sum+=rank[num[1]]
    return sum

# Dealer's turn after user "Stand" 
def dealer():
    while handsum(cpuhand)<=17:
        getcard=DrawCard(getdeck)
        cpuhand.append(getcard.mycard)
        print("\n CPU Hand--> ")
        showhand(cpuhand) 
        
# Check for Double Jack            
def double_jack():
    
    global total_money
    global bet
    if len(userhand)==2 and handsum(userhand)==21:
        clear_output()
        print("\n Your Hand--> ") 
        showhand(userhand)
        print(f" Your Hand Score: {handsum(userhand)}")
        print(" BlackedJack! \n You won the bet with 1.5x Bonus.")
        bet*=1.5
        total_money+=bet
        print(f" Wallet: {total_money}")
        return False
    else:
        if handsum(userhand)==21:
            clear_output()
            print("\n Your Hand--> ") 
            showhand(userhand)
            print(f" Your Hand Score: {handsum(userhand)}")
            print(" Score! \n You won the bet ")
            total_money+=bet
            print(f" Wallet: {total_money}")
            return False
    
    if handsum(userhand)>21:
        clear_output()
        print("\n Your Hand--> ") 
        showhand(userhand)
        print(f" Your Hand Score: {handsum(userhand)}")
        print(" BUSTED ;) \n You lost the bet ;)")
        total_money-=bet
        print(f"Wallet: {total_money}")
        return False
    
    return True
    
# Final winner after dealer's turn        
def check_jack(usersum,cpusum):
    
    global total_money
    global bet
    clear_output()
    print("\n Your Hand--> ") 
    showhand(userhand)
    print("\n CPU Hand--> ")
    showhand(cpuhand)
    
    print(f" Your Hand Score: {usersum}")
    print(f" Dealer's Hand Score: {cpusum}")
    if cpusum<=21:
        if usersum > cpusum:
            print(" Score! \n You won the bet.")
            total_money+=bet
        
        elif usersum < cpusum:
            print(" Whoops ;) \n You lost the bet ;)")
            total_money-=bet
        else:
            print(" Game Tied \n Bets Pushed Back")
            
    else:
        print(" Dealer got Busted")
        print(" Score! \n You won the bet.")
        total_money+=bet
    
    print(f"Wallet: {total_money}")    

# Main Program        

print("\t\t Welcome to BlackedJack ")
print(f"\n You have been given starting bonus of ₹{total_money}\n You can earn more by winning games ")
print(" Minimum betting amount is ₹10, so Bet wisely.\n Enjoy the game")

print("\n 1) Start Game \n 2) Exit")
cmd=input("\n Input your Choice:")


while cmd=='1' and total_money!=0:
    
    # Place your bets
    print(f" Wallet: {total_money}")
    bet=betting()
    
    # Getting deck and Initialising Hands(Cards in hand) 
    getdeck=Deck()
    userhand=[]
    cpuhand=[]
    
    # Starting Game Orderly
    Deal()
    forward=user_choice()
    if forward==True:
        dealer()
        check_jack(handsum(userhand),handsum(cpuhand))
    
    print("\n 1) Continue \n 2) Exit")
    cmd=input("\n Input your Choice:")
    clear_output()
else:
    clear_output()
    if total_money<=0:
        print(f"Wallet: {total_money}")
        print("Game Over")
    print("\n THANK YOU ")
    
