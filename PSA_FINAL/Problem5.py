import hashlib
import random

n = int(input("Сколько др ты хочешь проверить: "))


def generate_random_birthdates(num_dates):
    birthdates = []
    for _ in range(num_dates):
        month = random.randint(1, 12)

        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        elif month == 2:
            day = random.randint(1, 28)
        else:
            day = random.randint(1, 30)

        date_str = f"{month:02d}-{day:02d}"
        md5_hash = hashlib.md5(date_str.encode()).hexdigest()
        birthdates.append(md5_hash)

    return birthdates


hashed_birthdates = generate_random_birthdates(n)
hashed_birthdates1 = generate_random_birthdates(n)


def check_common_elements(list1, list2):
    common_elements = []

    for element in list1:
        if element in list2:
            common_elements.append(element)

    return common_elements


list1 = hashed_birthdates
list2 = hashed_birthdates1
common_elements = check_common_elements(list1, list2)


print(hashed_birthdates)
print(
    "-----------------------------------------------------------------------------------------------------------------"
)
print(hashed_birthdates1)
print(
    "-----------------------------------------------------------------------------------------------------------------"
)
if common_elements:
    print("Списки содержат общие элементы:", common_elements)
else:
    print("Списки не содержат общих элементов.")
