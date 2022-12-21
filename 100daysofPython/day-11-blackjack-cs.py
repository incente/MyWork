import random

def card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def print_scores(player, dealer):
    print(f"Player: {player}, current score {sum(player)}")
    print(f"Dealer: {dealer}, current score {sum(dealer)}")

def deal(player, dealer):
    player.append(card())
    player.append(card())
    dealer.append(card())
    hit_stand(player, dealer)

def hit_stand(player, dealer):
    print_scores(player, dealer)
    choose = input("Type 'hit' or 'stand': ")
    if choose.lower() == "hit":
        hit(player, dealer)
    elif choose.lower() == "stand":
        stand(player, dealer)
    else:
        print("Wrong input, only 'hit' and 'stand' are possible calls.")
        hit_stand(player, dealer)

def check_hit(player, dealer):
    if sum(player) > 21:
        print_scores(player, dealer)
        print("Lose")
    else:
        hit_stand(player, dealer)

def check_stand(player, dealer):
    if sum(dealer) > 21:
        print("Win")
    elif sum(player) > sum(dealer):
        print("Win")
    elif sum(player) < sum(dealer):
        print("Lose")
    else:
        print("Push")

def hit(player, dealer):
    player.append(card())
    check_hit(player, dealer)

def stand(player, dealer):
    while sum(dealer) < 17:
        dealer.append(card())
    print_scores(player, dealer)
    check_stand(player, dealer)

deal(player=[], dealer=[])