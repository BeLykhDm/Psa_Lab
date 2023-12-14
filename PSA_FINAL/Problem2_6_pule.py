import random


def game():  # РЯДОМ + РАНДОМ
    win = 0
    my = [1, 2, 3, 4, 5, 6]
    my_list = [1, 2, 3, 4, 5, 6]
    pulea_1 = random.choice(my)

    if pulea_1 == 6:
        pulea_2 = 1
    else:
        pulea_2 = pulea_1 + 1

    game_list = my_list
    game_list.remove(pulea_1)
    game_list.remove(pulea_2)

    choice = random.choice(my_list)
    my.remove(choice)

    life = random.choice(my)

    if life != pulea_1 and life != pulea_2:
        win += 1
    return win


def game2():  # РЯДОМ + ОСТАВИТЬ
    win = 0
    my = [1, 2, 3, 4, 5, 6]
    my_list = [1, 2, 3, 4, 5, 6]
    pulea_1 = random.choice(my)

    if pulea_1 == 6:
        pulea_2 = 1
    else:
        pulea_2 = pulea_1 + 1
    game_list = my_list
    game_list.remove(pulea_1)
    game_list.remove(pulea_2)

    choice = random.choice(my_list)
    my.remove(choice)

    if choice == 6:
        life = 1
    else:
        life = choice + 1

    if life != pulea_1 and life != pulea_2:
        win += 1
    return win


def game3():  # РАЗНЫЕ + РАНДОМ
    my = [1, 2, 3, 4, 5, 6]
    my_list = [1, 2, 3, 4, 5, 6]
    win = 0

    pulea_1 = random.choice(my)
    game_list = my_list
    game_list.remove(pulea_1)

    if pulea_1 == 6:
        a = 1
    else:
        a = pulea_1 + 1
    if pulea_1 == 1:
        b = 6
    else:
        b = pulea_1 - 1

    pulea_2 = random.choice(my_list)
    while pulea_2 == a or pulea_2 == b:
        pulea_2 = random.choice(my_list)
    game_list.remove(pulea_2)
    choice = random.choice(my_list)
    my.remove(choice)

    life = random.choice(my)

    if life != pulea_1 and life != pulea_2:
        win += 1
    return win


def game4():  # РАЗНЫЕ + ОСТАВИТЬ
    my = [1, 2, 3, 4, 5, 6]
    my_list = [1, 2, 3, 4, 5, 6]

    win = 0
    pulea_1 = random.choice(my)
    game_list = my_list
    game_list.remove(pulea_1)

    if pulea_1 == 6:
        a = 1
    else:
        a = pulea_1 + 1
    if pulea_1 == 1:
        b = 6
    else:
        b = pulea_1 - 1

    pulea_2 = random.choice(my_list)
    while pulea_2 == a or pulea_2 == b:
        pulea_2 = random.choice(my_list)
    game_list.remove(pulea_2)

    choice = random.choice(my_list)
    my.remove(choice)
    if choice == 6:
        life = 1
    else:
        life = choice + 1

    if life != pulea_1 and life != pulea_2:
        win += 1
    return win


def simulate(num_games):
    total_payout = 0
    for i in range(num_games):
        total_payout += game()
    probability = total_payout / num_games
    return probability


num_games = 100000
probability = simulate(num_games)


def simulate1(num_games):
    total_payout2 = 0
    for i in range(num_games):
        total_payout2 += game2()
    probability_of_not_changing = total_payout2 / num_games
    return probability_of_not_changing


num_games = 100000
probability_of_not_changing = simulate1(num_games)


def simulate2(num_games):
    total_payout3 = 0
    for i in range(num_games):
        total_payout3 += game3()
    pr = total_payout3 / num_games
    return pr


num_games = 100000
pr = simulate2(num_games)


def simulate3(num_games):
    total_payout4 = 0
    for i in range(num_games):
        total_payout4 += game4()
    pro = total_payout4 / num_games
    return pro


num_games = 100000
pro = simulate3(num_games)

print(f"Probability 1 to be survive in {num_games} games is: {probability:}")
print(
    f"Probability 2 to be survive in {num_games} games is: {probability_of_not_changing:}"
)
print(f"Probability 3 to be survive in {num_games} games is: {pr:}")
print(f"Probability 4 to be survive in {num_games} games is: {pro:}")
