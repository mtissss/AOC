with open("D:\\Programowanie\\Repo\\AOC\\2024\\data24_4.txt", "r") as file:
    data = file.read().strip().split("\n")

# data = """
# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# .........."""

# data = data.strip().split("\n")
# print(data)


def adv4_1(data):
    def create_coordinates(data):
        coordinates = {}
        # Iterating by rows
        for y, line in enumerate(data, start=0):  # y is number of row, start from 0
            # Iterating by columns
            for x, char in enumerate(
                line, start=0
            ):  # x is number of column, start from 0
                coordinates[(x, y)] = char
        return coordinates

    def length_of_matrix(data):
        # checking length of data
        lines = len(data)
        columns = len(data[0]) if lines > 0 else 0
        return lines, columns

    def get_letter_by_coordinates(coordinates, x, y):
        # Coordinates (x,y) to search variable in dictionary
        return coordinates.get(
            (x, y), None
        )  # If coordinates doesn't exist, return none

    lines, columns = length_of_matrix(data)
    coordinates = create_coordinates(data)

    def vertical_search(coordinates, lines, columns):
        counter1 = 0
        for x in range(columns):  # Checking horizontal from left to right
            for y in range(lines):
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "X"
                    and get_letter_by_coordinates(coordinates, x, y + 1) == "M"
                    and get_letter_by_coordinates(coordinates, x, y + 2) == "A"
                    and get_letter_by_coordinates(coordinates, x, y + 3) == "S"
                ):
                    counter1 += 1
        for x in range(columns):  # Checking horizontal from right to left
            for y in range(lines - 1, -1, -1):
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "X"
                    and get_letter_by_coordinates(coordinates, x, y - 1) == "M"
                    and get_letter_by_coordinates(coordinates, x, y - 2) == "A"
                    and get_letter_by_coordinates(coordinates, x, y - 3) == "S"
                ):
                    counter1 += 1

        # if counter1 > 0:
        #     print("Znaleziono xmas v", counter1, "razy")
        # else:
        #     print("nie znaleziono: xmas v")
        return counter1

    def horizontal_search(coordinates, lines, columns):
        counter2 = 0
        for y in range(lines):
            for x in range(columns):  # Chcecking vertical from left to right
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "X"
                    and get_letter_by_coordinates(coordinates, x + 1, y) == "M"
                    and get_letter_by_coordinates(coordinates, x + 2, y) == "A"
                    and get_letter_by_coordinates(coordinates, x + 3, y) == "S"
                ):
                    counter2 += 1

        for y in range(lines):
            for x in range(
                columns - 1, -1, -1
            ):  # Chcecking vertical from right to left
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "X"
                    and get_letter_by_coordinates(coordinates, x - 1, y) == "M"
                    and get_letter_by_coordinates(coordinates, x - 2, y) == "A"
                    and get_letter_by_coordinates(coordinates, x - 3, y) == "S"
                ):
                    counter2 += 1
        # if counter2 > 0:
        #     print("Znaleziono xmas h", counter2, "razy")
        # else:
        #     print("nie znaleziono: xmas h")
        return counter2

    def diagonal_right_search(coordinates, lines, columns):

        counter3 = 0
        for x in range(columns):  # Checking across from left to right and down >v
            for y in range(lines):
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "X"
                    and get_letter_by_coordinates(coordinates, x + 1, y + 1) == "M"
                    and get_letter_by_coordinates(coordinates, x + 2, y + 2) == "A"
                    and get_letter_by_coordinates(coordinates, x + 3, y + 3) == "S"
                ):
                    counter3 += 1

        for x in range(
            columns - 1, 2, -1
        ):  # Checking across from right to left and up <^
            for y in range(lines - 1, 2, -1):
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "X"
                    and get_letter_by_coordinates(coordinates, x - 1, y - 1) == "M"
                    and get_letter_by_coordinates(coordinates, x - 2, y - 2) == "A"
                    and get_letter_by_coordinates(coordinates, x - 3, y - 3) == "S"
                ):
                    counter3 += 1
        # if counter3 > 0:
        #     print("Znaleziono xmas SKOS PRAWY", counter3, "razy")
        # else:
        #     print("nie znaleziono: xmas")
        return counter3

    def diagonal_left_search(coordinates, lines, columns):
        counter4 = 0

        for x in range(
            columns - 1, 2, -1
        ):  # Checking across from right to left and down <v
            for y in range(lines):
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "X"
                    and get_letter_by_coordinates(coordinates, x - 1, y + 1) == "M"
                    and get_letter_by_coordinates(coordinates, x - 2, y + 2) == "A"
                    and get_letter_by_coordinates(coordinates, x - 3, y + 3) == "S"
                ):
                    counter4 += 1
        for x in range(columns):
            for y in range(
                lines - 1, 2, -1
            ):  # Checking across from left to right and up >^
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "X"
                    and get_letter_by_coordinates(coordinates, x + 1, y - 1) == "M"
                    and get_letter_by_coordinates(coordinates, x + 2, y - 2) == "A"
                    and get_letter_by_coordinates(coordinates, x + 3, y - 3) == "S"
                ):
                    counter4 += 1

        # if counter4 > 0:
        #     print("Znaleziono xmas SKOS lewy", counter4, "razy")
        # else:
        #     print("nie znaleziono: xmas")
        return counter4

    a = vertical_search(coordinates, lines, columns)
    b = horizontal_search(coordinates, lines, columns)
    c = diagonal_right_search(coordinates, lines, columns)
    d = diagonal_left_search(coordinates, lines, columns)
    e = a + b + c + d
    return e


def adv4_2(data):
    def create_coordinates(data):
        coordinates = {}
        # Iterating by rows
        for y, line in enumerate(data, start=0):  # y is number of row, start from 0
            # Iterating by columns
            for x, char in enumerate(
                line, start=0
            ):  # x is number of column, start from 0
                coordinates[(x, y)] = char
        return coordinates

    def length_of_matrix(data):
        # checking length of data
        lines = len(data)
        columns = len(data[0]) if lines > 0 else 0
        return lines, columns

    def get_letter_by_coordinates(coordinates, x, y):
        # Coordinates (x,y) to search variable in dictionary
        return coordinates.get(
            (x, y), None
        )  # If coordinates doesn't exist, return none

    lines, columns = length_of_matrix(data)
    coordinates = create_coordinates(data)

    def m_search(coordinates, lines, columns):
        counter1 = 0
        for x in range(columns):  # Checking horizontal from left to right
            for y in range(lines):
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "M"
                    and get_letter_by_coordinates(coordinates, x + 2, y) == "M"
                    and get_letter_by_coordinates(coordinates, x + 1, y + 1) == "A"
                    and get_letter_by_coordinates(coordinates, x, y + 2) == "S"
                    and get_letter_by_coordinates(coordinates, x + 2, y + 2) == "S"
                ):
                    counter1 += 1
        for x in range(columns):  # Checking horizontal from right to left
            for y in range(lines):
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "M"
                    and get_letter_by_coordinates(coordinates, x + 2, y) == "S"
                    and get_letter_by_coordinates(coordinates, x + 1, y + 1) == "A"
                    and get_letter_by_coordinates(coordinates, x, y + 2) == "M"
                    and get_letter_by_coordinates(coordinates, x + 2, y + 2) == "S"
                ):
                    counter1 += 1

        # if counter1 > 0:
        #     print("Znaleziono mas M", counter1, "razy")
        # else:
        #     print("nie znaleziono: mas M")
        return counter1

    def s_search(coordinates, lines, columns):
        counter2 = 0
        for x in range(columns):  # Checking horizontal from left to right
            for y in range(lines):
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "S"
                    and get_letter_by_coordinates(coordinates, x + 2, y) == "M"
                    and get_letter_by_coordinates(coordinates, x + 1, y + 1) == "A"
                    and get_letter_by_coordinates(coordinates, x, y + 2) == "S"
                    and get_letter_by_coordinates(coordinates, x + 2, y + 2) == "M"
                ):
                    counter2 += 1
        for x in range(columns):  # Checking horizontal from right to left
            for y in range(lines):
                if (
                    get_letter_by_coordinates(coordinates, x, y) == "S"
                    and get_letter_by_coordinates(coordinates, x + 2, y) == "S"
                    and get_letter_by_coordinates(coordinates, x + 1, y + 1) == "A"
                    and get_letter_by_coordinates(coordinates, x, y + 2) == "M"
                    and get_letter_by_coordinates(coordinates, x + 2, y + 2) == "M"
                ):
                    counter2 += 1

        # if counter2 > 0:
        #     print("Znaleziono mas M", counter2, "razy")
        # else:
        #     print("nie znaleziono: mas M")
        return counter2

    a = m_search(coordinates, lines, columns)
    b = s_search(coordinates, lines, columns)
    e = a + b
    return e


print(f"Wynik części pierwszej: {adv4_1(data)}\nWynik części drugiej: {adv4_2(data)}")
