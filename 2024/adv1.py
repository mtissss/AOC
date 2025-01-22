with open("D:\\Programowanie\\Repo\\AOC\\2024\\data24_1.txt", "r") as file:
    data = file.read().strip().split("\n")


def adv1_1(data):
    # def new lists
    col_1 = []
    col_2 = []

    # converting colums into list
    for x in data:
        x = x.split("   ")
        col_1.append(int(x[0]))
        col_2.append(int(x[1]))

    # sorting list
    col_1.sort()
    col_2.sort()
    sum_all = 0

    # calculating distance between every pair of numbers (with the same index) from list col1 and col2
    for x in range(len(col_1)):
        distance = abs(col_1[x] - col_2[x])
        sum_all += distance
    return sum_all


def adv1_2(data):
    # def new lists
    col_1 = []
    col_2 = []
    sum_all = 0

    # converting colums into list
    for x in data:
        x = x.split("   ")
        col_1.append(int(x[0]))
        col_2.append(int(x[1]))

    for x in range(len(col_1)):
        # counting ocurrences element from list col1 in list col2
        y = col_2.count(col_1[x])
        # calculating similarity score
        similarity_score = int(y * col_1[x])
        sum_all += similarity_score
    return sum_all


print(f"Wynik części pierwszej: {adv1_1(data)}\nWynik części drugiej: {adv1_2(data)}")
