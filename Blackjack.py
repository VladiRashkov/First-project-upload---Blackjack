import random

def welcome():
    welcome_message = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    count = 0
    while welcome_message == "y":
        count += 1
        if count >= 2:
            welcome_message = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            if welcome_message == "n":
                welcome_message = " "
                break

        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 5

        user_hand = []
        current_userscore = 0
        comp_hand = []
        current_compscore = 0
        for _ in range(2):
            # picks the first two cards for the user
            user_hand.append(random.choice(cards))

        current_userscore = sum(user_hand)
        #first hand for the computer  
        comp_hand.append(random.choice(cards))
        current_compscore = sum(comp_hand)
        print(f"Your cards: {user_hand}, current score: {current_userscore}")
        print(f"Computer's first card: {comp_hand}")

        def comp_hit():
            comp_hand.append(random.choice(cards))
            return comp_hand

        def user_hit():
            user_hand.append(random.choice(cards))
            return user_hand

        while True:
            if current_userscore > 21:
                print("You lose!")
                break
            elif current_userscore == 21:
                comp_hit()
                current_compscore += comp_hand[-1]
                if current_userscore == current_compscore:
                    print(
                        (f"Your cards: {user_hand}, current score: {current_userscore}"))
                    print(
                        f"Computer's final hand: {comp_hand}, final score: {current_compscore}")
                    print("Draw!")
                    break
                else:
                    print(
                        (f"Your cards: {user_hand}, current score: {current_userscore}"))
                    print(
                        f"Computer's final hand: {comp_hand}, final score: {current_compscore}")
                    print("You win!")
                    break
            elif current_userscore < 21:
                new_message = input(
                    "Type 'y' to get another card, type 'n' to pass: ")
                if new_message == "y":
                    user_hit()
                    current_userscore += user_hand[-1]
                    if current_userscore > 21 and 11 in user_hand:
                        current_userscore -= 10
                        print(
                            (f"Your cards: {user_hand}, current score: {current_userscore}"))
                        print(f"Computer's first card: {comp_hand}")
                    elif current_userscore > 21:
                        print(f"Your score is {current_userscore}")
                        print("You lose!")
                        welcome_message = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                        break
                    elif current_userscore == 21:
                        comp_hit()
                        current_compscore += comp_hand[-1]
                        if current_userscore == current_compscore:
                            print(
                                (f"Your cards: {user_hand}, current score: {current_userscore}"))
                            print(
                                f"Computer's final hand: {comp_hand}, final score: {current_compscore}")
                            print("Draw!")
                            break
                    else:
                        print(
                            (f"Your cards: {user_hand}, current score: {current_userscore}"))
                        print(f"Computer's first card: {comp_hand}")
                else:
                    comp_hit()
                    current_compscore += comp_hand[-1]
                    if current_compscore > 21:
                        if 11 in comp_hand:
                            current_compscore -= 10
                    while current_compscore < current_userscore:
                        comp_hit()
                        current_compscore += comp_hand[-1]

                    if current_compscore > 21:
                        print(
                            (f"Your cards: {user_hand}, current score: {current_userscore}"))
                        print(
                            f"Computer's final hand: {comp_hand}, final score: {current_compscore}")
                        print("You win!")
                        break
                    elif current_compscore == current_userscore:
                        print(
                            (f"Your cards: {user_hand}, current score: {current_userscore}"))
                        print(
                            f"Computer's final hand: {comp_hand}, final score: {current_compscore}")
                        print("Draw!")
                        break
                    else:
                        print(
                            (f"Your cards: {user_hand}, current score: {current_userscore}"))
                        print(
                            f"Computer's final hand: {comp_hand}, final score: {current_compscore}")
                        print("You lose!")
                        break
            elif current_compscore == 21:
                print(
                    (f"Your cards: {user_hand}, current score: {current_userscore}"))
                print(
                    f"Computer's final hand: {comp_hand}, final score: {current_compscore}")
                print("You lose!")
                break
    return welcome_message
print("Thank you for playing!", welcome())
