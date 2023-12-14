import random

list_red = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
game_list = list(range(0, 36))

lose_list = []
n = 1000
for i in range(n):
    balance = 100
    stavka = 1
    while balance <= 105 and balance >= -100:
        if balance < stavka:
            minus = balance - stavka
            lose_list.append(minus)
            break
        choice = random.choice(game_list)
        if choice in list_red:
            balance += stavka
            stavka = 1
        else:
            balance -= stavka
            stavka = stavka * 2
sum_lose = sum(lose_list)
print("Avarage lose: " + str(sum_lose / len(lose_list)))
print("Все деньги который ты проиграл за " + str(n) + " games is: " + str(sum_lose))
win = 1 - len(lose_list) / n
print("Probability to win " + str(win))
print("Probability to lose is: " + str(len(lose_list) / n))
math_expectation = (sum_lose / len(lose_list)) * len(lose_list) / n + 5 * (
    1 - len(lose_list) / n
)
print(f"Mathematical expectation is: {math_expectation}")
