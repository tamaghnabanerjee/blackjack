import random
import sys
import os
import time

os.system('clear')
deck = ['A',2,3,4,5,6,7,8,9,10,10,10,10]

user_cards_drawn = []
computer_cards_drawn = []
sum_user = 0
sum_computer= 0
withdraw = False
blackjack = False
A_counter = 0

def user_continue(user_cards_drawn,how_many=1):
    global sum_user,A_counter, blackjack
    for i in range(how_many):
        user_card = random.choice(deck)
        if user_card == 'A':
            A_counter += 1
            if sum_user + 11 <= 21:
                user_card = 11
            else:
                user_card = 1
        user_cards_drawn.append(user_card)
        sum_user = sum(user_cards_drawn)
        
        if sum_user == 21:
            blackjack = True
        elif sum_user > 21 and A_counter > 0:
            sum_user = sum_user - 10
            print("10 deducted")
            print("after deduction sum user", sum_user)
    print("Your cards: ")
    for i in user_cards_drawn:
        print(i)
    print("Sum: ", sum_user)

def computer_continue(computer_cards_drawn):
    global sum_computer, A_counter
    computer_card = random.choice(deck)
    if computer_card == 'A':
        A_counter += 1
        if sum_computer + 11 <= 21:
            computer_card = 11
        else:
            computer_card = 1
    computer_cards_drawn.append(computer_card)
    sum_computer = sum(computer_cards_drawn)
    
    if sum_computer > 21 and A_counter > 0:
        sum_computer = sum_computer - 10
        print("10 deducted")
        print("after deduction sum user", sum_computer)

    if sum_computer > 21 and A_counter > 0:
        sum_computer -= 10
    print("Dealer cards: ",computer_cards_drawn[0])

def computer_show(computer_cards_drawn):
    global sum_computer, withdraw
    computer_card = random.choice(deck)
    if computer_card == 'A':
            if sum_computer + 11 <= 21:
                computer_card = 11
            else:
                computer_card = 1
    computer_cards_drawn.append(computer_card)
    sum_computer = sum(computer_cards_drawn)

    if sum_computer > 21 and A_counter > 0:
        sum_computer = sum_computer - 10
        print("10 deducted")
        print("after deduction sum user", sum_computer)

    print("Dealer cards: ")
    for i in computer_cards_drawn:
        time.sleep(1)
        print(i)
    print("Sum: ", sum_computer)
    if sum_computer >= 17 and sum_computer <= 21:
        withdraw = True


def winner(sum_user,sum_computer):
    if not withdraw:
        if sum_user > 21 or sum_computer > 21:
            if sum_user == sum_computer:
                return 'draw'
            elif sum_user > sum_computer:
                return 'dealer'
            else:
                return 'user'
    elif sum_computer > sum_user:
        return 'dealer'
    elif sum_computer < sum_user:
        return 'user'
    elif sum_computer == sum_user:
        return 'draw'
    else:
        return False


def main():
    computer_continue(computer_cards_drawn)
    user_continue(user_cards_drawn,2)
    if blackjack:
        print('user')
        sys.exit()
        
    while True:
        user_choice = input("hit or stand?\n").lower()

        if user_choice == 'hit':
            user_continue(user_cards_drawn)
            if winner(sum_user,sum_computer):
                print(winner(sum_user,sum_computer))
                break
            else:
                continue
        
        elif user_choice == 'stand':
            while not winner(sum_user,sum_computer) and not withdraw:
                computer_show(computer_cards_drawn)
            print(winner(sum_user,sum_computer))
            break
    
main()  
