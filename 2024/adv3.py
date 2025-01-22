# with open("D:\\Programowanie\\Repo\\AOC\\2024\\data24_3.txt", "r") as file:
#     data = file.read().strip()
data = """!mul(417,528)why();what()?how()from()who()where() ~mul(215,18){} ])/from()*do(),)* ##select()mul(89,59):*select(805,600)*mul(709,138)-!how()$+*why(747,290)don't()>mul(548,826)^@-^%@,@mul(103,952)^why():mul(322,877)select()+who()%?[mul(378,598)<;[&(-*' mul(695,169)??where()mul(12,677){$?:(}*why()mul(911,924) *+/select()*/?,from(952,471)mul(12,238)<why()#<: mul(17,995)+:]mul(619,259)+$,#"""


def adv3_1(data):

    index = 0
    sum_symbols = 0
    number = ""
    n_chars = []

    for char in data:
        if char.isdigit():
            number += char
        else:
            if number:
                n_chars.append(number)
                number = ""
            n_chars.append(char)

    for index in range(len(n_chars)):
        flag = 0
        g = n_chars[index]
        if n_chars[index] == "m":
            index += 1
            if n_chars[index] == "u":
                index += 1
                if n_chars[index] == "l":
                    index += 1
                    if n_chars[index] == "(":
                        index += 1
                        if n_chars[index].isdigit():
                            a = int(n_chars[index])
                            index += 1
                            if n_chars[index] == ",":
                                index += 1
                                if n_chars[index].isdigit():
                                    b = int(n_chars[index])
                                    index += 1
                                    if n_chars[index] == ")":
                                        c = a * b
                                        flag = 1
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
        index += 1
        if flag == 1:
            sum_symbols += c
    return sum_symbols


def adv3_2(data):

    n_chars = []
    number = ""

    for char in data:
        if char.isdigit():
            number += char
        else:
            if number:
                n_chars.append(number)
                number = ""
            n_chars.append(char)

    def checking_do(n_chars, do, index):

        start_index = index
        for index in range(start_index, len(n_chars)):
            if n_chars[index] == "d":
                index += 1
                if n_chars[index] == "o":
                    index += 1
                    if n_chars[index] == "n":
                        index += 1
                        if n_chars[index] == "'":
                            index += 1
                            if n_chars[index] == "t":
                                index += 1
                                if n_chars[index] == "(":
                                    index += 1
                                    if n_chars[index] == ")":
                                        do = 0
                                        break
                                    else:
                                        break
                                else:
                                    break
                            else:
                                break
                        else:
                            break
                    else:
                        if n_chars[index] == "(":
                            index += 1
                            if n_chars[index] == ")":
                                do = 1
                            else:
                                break
                        else:
                            break
                else:
                    break
            else:
                break
        return do

    def checking_chars(data):

        do = 1
        index = 0
        sum_symbols = 0

        for index in range(len(n_chars)):
            flag = 0
            if n_chars[index] == "d":
                do = checking_do(n_chars, do, index)
                continue
            elif n_chars[index] == "m":
                index += 1
                if n_chars[index] == "u":
                    index += 1
                    if n_chars[index] == "l":
                        index += 1
                        if n_chars[index] == "(":
                            index += 1
                            if n_chars[index].isdigit():
                                a = int(n_chars[index])
                                index += 1
                                if n_chars[index] == ",":
                                    index += 1
                                    if n_chars[index].isdigit():
                                        b = int(n_chars[index])
                                        index += 1
                                        if n_chars[index] == ")":
                                            c = a * b
                                            flag = 1
                                        else:
                                            continue
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
            index += 1
            if flag == 1 and do == 1:
                sum_symbols += c
        return sum_symbols

    return checking_chars(data)


print(f"Wynik części pierwszej: {adv3_1(data)}\nWynik części drugiej: {adv3_2(data)}")
