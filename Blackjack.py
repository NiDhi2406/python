import random, sys
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'
def main():
    print('''
          Rules:
          try to get as close to 21 without going over.
          Kings, Queens, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points.
          Cards 2 through 10 are worth their face value.
          (H)it to take another card.
          (S)tand to stop taking cards.
          on your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17.
          ''')
    money = 5000
    while True:
        if money <= 0:
            print("You are broke!")
            print("Good things you were not playing with real money.")
            print("Thanks for playing!")
            sys.exit()
        print("Money:", money)
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        print("Bet:", bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)
            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("Bet increades to {}.".format(bet))
                print("Bet:", bet)
            if move in ('H', "D"):
                newCard = deck.pop()
                rank, suit = newCard
                print("You drew a {} of {}.".format(rank, suit))
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
                if move in ('S', 'D'):
                    break
            if getHandValue(playerHand) <= 21:
                    while getHandValue(dealerHand) < 17:
                        print("Dealer hits...")
                        dealerHand.append(deck.pop())
                        displayHands(playerHand, dealerHand, False)
                        if getHandValue(dealerHand) > 21:
                            break
                        input("Press enter to continue..")
                        print('\n\n')
                    
            displayHands(playerHand, dealerHand, True)
                
                    