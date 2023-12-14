import hashlib
import random

n = int(input("Сколько др ты хочешь проверить: "))
count = 0
games = 10000
for i in range(games):

    def generate_random_birthdates(num_dates, bits=40):
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
            md5_hash = hashlib.md5(date_str.encode()).hexdigest()[
                : bits // 4
            ]  # Усекаем до 40 бит
            birthdates.append(md5_hash)

        return birthdates

    hashed_birthdates = generate_random_birthdates(n, bits=40)
    hashed_birthdates1 = generate_random_birthdates(n, bits=40)

    def check_common_elements(list1, list2):
        common_elements = []

        for element in list1:
            if element in list2:
                common_elements.append(element)

        return common_elements

    list1 = hashed_birthdates
    list2 = hashed_birthdates1
    common_elements = check_common_elements(list1, list2)

    if len(common_elements) > 0:
        count += 1


print(count / games)
