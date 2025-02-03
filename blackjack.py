import random

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

    def __init__(self, name):
        self.name = name

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

class Blackjack():

    def __init__(self):
        self.pack = Pack()
        self.dealer = Player('The dealer')
        self.player = Player(input('Please enter your name: '))

    def play(self):
        self.deal_new_hands()
        twist_or_stick = input(f'Would {self.player.name} like to twist or stick (t or s): ').lower()
        if twist_or_stick == 't':
            self.twist_loop()
        if self.player.total() > 21:
            print(f'Bust! {self.player.name} loses!')
            return
        if self.player.total() == 21:
            print(f'Pontoon! {self.player.name} wins!')
            return
        print(f'Now {self.dealer.name} will play...')
        while self.dealer.total() <= self.player.total():
            self.dealer.twist(self.pack)
        self.dealer.print_hand()
        if self.dealer.total() > 21:
            print(f'{self.dealer.name} has bust. {self.player.name} wins!')
        elif self.dealer.total() == 21:
            print(f'{self.dealer.name} has scored 21. {self.dealer.name} wins!')
        else:
            print(f"{self.dealer.name}'s score of {self.dealer.total()} beats {self.player.name}'s score of {self.player.total()}. {self.dealer.name} wins!")

    def twist_loop(self):
        choice = 't'
        while choice == 't':
            self.player.twist(self.pack)
            self.player.print_hand()
            if self.player.total() >= 21: return
            choice = input(f'Would {self.player.name} like to twist or stick (t or s): ').lower()

    def deal_new_hands(self):
        self.dealer.new_hand(self.pack)
        self.dealer.print_hand()
        self.player.new_hand(self.pack)
        self.player.print_hand()

def main():
    print('\nWelcome to Blackjack.')
    blackjack = Blackjack()
    play_or_quit = 'p'
    while play_or_quit == 'p':
        blackjack.play()
        play_or_quit = input('Do you want to quit (q) or play again (p)? ')

main()
