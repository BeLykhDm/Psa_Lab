import random

number_of_experement = 730
pay_of = 0
penalization = 0
for i in range(number_of_experement):
    experement = random.uniform(0, 1.0)
    if experement > 0.02:
        exp2 = random.uniform(0, 1.0)
        if exp2 <= 0.05:
            penalization += 1
    else:
        pay_of += 1
normal_human = 365 * 2 * 720
pay = penalization * 300 - 350 + pay_of * 6

print(f"Dodik Jora Petrovic pay per year: {pay}")
print(f"Normal Student pays: {normal_human}")
