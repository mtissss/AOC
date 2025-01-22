with open("D:\\Programowanie\\Repo\\AOC\\2024\\data24_5.txt", "r") as file:
    data = file.read().strip().split("\n")


def adv5_1(data):
    # Lists to store coordinates and numbers
    coordinates = []  # List of coordinate pairs
    number_sets = []  # List of numbers from each line

    # Processing input data
    for line in data:
        if "|" in line:
            coordinates.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            number_sets.append(list(map(int, line.split(","))))

    # Function to check the validity of the numbers list
    def is_valid(numbers, coordinates):
        for cord in coordinates:
            if cord[0] in numbers and cord[1] in numbers:
                index1 = numbers.index(cord[0])
                index2 = numbers.index(cord[1])
                if index1 > index2:
                    # print(f"Conflict found: {cord[0]} appears after {cord[1]}")
                    return False
        return True

    suma = 0
    # Checking the validity of each list of numbers
    for numbers in number_sets:
        if is_valid(numbers, coordinates):
            # print(f"List {numbers} is valid.")
            suma += numbers[int((len(numbers)) / 2)]
        else:
            # print(f"List {numbers} is invalid.")
            continue
    print(f"{suma} is the sum of the middle numbers of the list")

    return suma


def adv5_2(data):
    # Lists to store coordinates and numbers
    coordinates = []  # List of coordinate pairs
    number_sets = []  # List of numbers from each line

    # Processing input data
    for line in data:
        if "|" in line:
            coordinates.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            number_sets.append(list(map(int, line.split(","))))

    # Function to check the validity of the numbers list
    def is_valid(numbers, coordinates):
        for cord in coordinates:
            if cord[0] in numbers and cord[1] in numbers:
                index1 = numbers.index(cord[0])
                index2 = numbers.index(cord[1])
                if index1 > index2:
                    return False
        return True

    # Function to correct the order of the numbers list
    def correct_order(numbers, coordinates):
        changed = True
        while changed:
            changed = False
            for cord in coordinates:
                if cord[0] in numbers and cord[1] in numbers:
                    index1 = numbers.index(cord[0])
                    index2 = numbers.index(cord[1])
                    if index1 > index2:
                        numbers[index1], numbers[index2] = (
                            numbers[index2],
                            numbers[index1],
                        )
                        changed = True
        return numbers

    suma = 0
    # Checking and correcting the order of each list of numbers
    for numbers in number_sets:
        if not is_valid(numbers, coordinates):
            numbers = correct_order(numbers, coordinates)
            suma += numbers[int((len(numbers)) / 2)]
    print(f"{suma} is the sum of the middle numbers of the list")

    return suma


print(f"Wynik części pierwszej: {adv5_1(data)}\nWynik części drugiej: {adv5_2(data)}")
