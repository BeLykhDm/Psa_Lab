particiants = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if particiants[-1] == particiants[-2] + 1 and particiants[0] == 0:
    print("ssss")


for i in range(len(particiants) - 1):
    if particiants[i] == particiants[i + 1] - 1 and particiants[i - 1] + 1:
        print(particiants[i])
