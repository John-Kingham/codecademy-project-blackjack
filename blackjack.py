import random

# The game has one dealer and one player.
# The goal is to have your cards total 21 or as close as possible without going over.
# Number cards have their face value, picture cards have a value of 10. Aces are 11.
# The dealer and player are dealt two cards. All cards are face up.
# The player plays first.
# When the game is loaded, it should tell the Player what cards the Dealer has and what cards the Player has.
# The player must choose twist or stick.
# If the player twists, the dealer gives the player another card. 
# If the player's hand totals 21, the dealer shouts "Pontoon!" and the player wins.
# If the player's hand is less than 21, they can twist again, or stick.
# If the player's hand goes over 21, the dealer shouts "Bust!" and the dealer wins.
# If the player sticks, the dealer runs through the same process of twisting or sticking until the dealer's total (a) beats the player's total or (b) goes bust. 
# If the dealer goes bust, the player wins.
# If the dealer's hand beats the player's, the dealer sticks and wins.

class Card():

    names_and_values = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,
                  'jack':10,'queen':10,'king':10,'ace':11}

    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.value = Card.names_and_values[name]

class Pack():

    def __init__(self):
        self.cards = []
        for suit in ('harts', 'diamonds', 'spades', 'clubs'):
            for name in Card.names_and_values.keys():
                self.cards.append(Card(name, suit))
        random.shuffle(self.cards)

    def top_card(self):
        return self.cards.pop()

class Player():

    def __init__(self, name, pack):
        self.name = name
        self.new_hand(pack)
    
    def twist(self, pack):
        self.hand.append(pack.top_card())

    def total(self):
        total = 0
        for card in self.hand:
            total += card.value
        return total
    
    def print_hand(self):
        print(f"\n{self.name}'s cards are:")
        for card in self.hand:
            print(f'{card.name} of {card.suit}')  
        print(f'Total = {self.total()}')

    def new_hand(self, pack):
        self.hand = []
        self.twist(pack)
        self.twist(pack)

def main():
    pack, dealer, player = initialise_game()
    player_choice = input(f'Would {player.name} like to twist or stick (t or s): ').lower()
    while player_choice == 't':
        player.twist(pack)
        player.print_hand()
        if player.total() >= 21: break
        player_choice = input(f'Would {player.name} like to twist or stick (t or s): ').lower()
    if player.total() > 21:
        print(f'Bust! {player.name} loses!')
        return
    if player.total() == 21:
        print(f'Pontoon! {player.name} wins!')
        return
    print(f'Now {dealer.name} will play...')
    while dealer.total() <= player.total():
        dealer.twist(pack)
    dealer.print_hand()
    if dealer.total() > 21:
        print(f'{dealer.name} has bust. {player.name} wins!')
    elif dealer.total() == 21:
        print(f'{dealer.name} has scored 21. {dealer.name} wins!')
    else:
        print(f"{dealer.name}'s score of {dealer.total()} beats {player.name}'s score of {player.total()}. {dealer.name} wins!")

def initialise_game():
    print('\nWelcome to Blackjack.')
    pack = Pack()
    dealer = Player('The dealer', pack)
    dealer.print_hand()
    player = Player(input('Please enter your name: '), pack)
    player.print_hand()
    return pack,dealer,player

main()
