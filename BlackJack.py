import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"] for v in range(1, 14)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value == 1:
                has_ace = True
            self.value += card.value
        if has_ace and self.value + 10 <= 21:
            self.value += 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1:])
        else:
            print(self.cards)
            print(f"Hand value: {self.get_value()}")


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Hand()
        self.dealer = Hand(dealer=True)

        for i in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

    def play(self):
        playing = True

        while playing:
            self.player.display()
            self.dealer.display()

            choice = input("Hit or stay?\nEnter H to hit or S to stay\n").lower()
            if choice == "h":
                self.player.add_card(self.deck.deal())
                if self.player.get_value() > 21:
                    playing = False
            else:
                playing = False

        if self.player.get_value() > 21:
            print("You have busted!")
        else:
            while self.dealer.get_value() < 17:
                self.dealer.add_card(self.deck.deal())

            if self.dealer.get_value() > 21:
                print("Dealer busts!")
            elif self.dealer.get_value() < self.player.get_value():
                print("You win!")
            elif self.dealer.get_value() > self.player.get_value():
                print("Dealer wins!")
            else:
                print("It's a tie!")

        game = Game()
        game.play()
