import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self,suits,rank):
        self.suits = suits
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f"{self.rank} of {self.suits}"

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit,rank)
                self.all_cards.append(new_card)
    def __str__(self):
        return f"Our deck> {self.all_cards}"
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal(self):
        card = self.all_cards.pop()
        return card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self, total = 100):
        self.total = total 
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(amount):
    while True:
        try:
            amount.bet = int(input("Please take a bet: "))
        except:
            print("You need to input a number!")
        else:
            if amount.bet > amount.total:
                print("You dont have enough chips")
            else:
                break

def hit(deck,hand):
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()

def split(desk,hand):
    pass

def hit_or_stand(deck,hand):
    global playing

    while True:
        player = input("Do you want to Hit or Stand: ")
        if player == 'Hit':
            hit(deck,hand)
        elif player == 'Stand':
            playing = False
        else:
            print("You need to select from: Hit/Stand")
            continue
        break

def show_some(player,dealer):
    print(f"Player value: {player.value} Dealer value: {dealer.cards[1].value}")
    print("Dealers hand: ")
    print("<hidden>")
    print(dealer.cards[1])
    print("Players hand:", *player.cards, sep='\n')
    '''
    for card in player.cards:
        print(card)
    '''
    
def show_all(player,dealer):
    print(f"Player value: {player.value} Dealer value: {dealer.value}")
    print("Dealer hand:", *dealer.cards, sep='\n')
    print("Player hand:", *player.cards, sep='\n')

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer,chips):
    print("Its a draw!")
    
while True:
    print("Hello, you are now playing BlackJack!")
    playing = True

    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing:
        
        hit_or_stand(deck,player_hand)
        
        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips) 
        else:
            push(player_hand,dealer_hand,player_chips)

    print(f"Total value of players chips: {player_chips.total}")
    answer = input("Do you want to play again? (y/n): ")
    if answer.lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
                