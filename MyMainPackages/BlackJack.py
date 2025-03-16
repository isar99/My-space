#define all the elements in cards

import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print("Mtlb yaar kuch bhi daaloge... Aise nhi hota hai integer daalo")
        else:
            if chips.bet > chips.total:
                print("Pocket mein paisa hai tmhreee?  Nhi n...", chips.total)
            else:
                break
                
def hit(deck,hand):
    
    hand.add_cards(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Would you like to HIT or STAND? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand) 
            
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing. ")
            playing = False
            
        else:
            print("Sorry, Please try again.")
            continue
        break

        
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.lose_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.win_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
    
while True:
    print("Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17 or above. Aces count as 1 or 11 as required.")
    
    # Create & shuffle the deck, deal two cards to each player 
    new_deck = Deck()
    new_deck.shuffle()
    
    player = Hand()
    player.add_cards(new_deck.deal_one())
    player.add_cards(new_deck.deal_one())
    
    dealer = Hand()
    dealer.add_cards(new_deck.deal_one())
    dealer.add_cards(new_deck.deal_one())
    
    # Set up the Player's chips
    player_chips = Chips() #default value is 100
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    
    while playing:
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(new_deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player,dealer,player_chips)
            break
            
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value < 21:
        
        while dealer.value < 17:
            hit(new_deck,dealer)
    
        # Show all cards
        show_all(player,dealer)
        
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player,dealer,player_chips)
        elif player.value > dealer.value:
            player_wins(player,dealer,player_chips)
        elif player.value < dealer.value:
            dealer_wins(player,dealer,player_chips)
        else:
            push(player,dealer)
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? 'y' or 'n'")
    
    if new_game[0].lower() == 'y':
        playing =True
        continue
        
    else:
        print("Thanks for playing!")
        break