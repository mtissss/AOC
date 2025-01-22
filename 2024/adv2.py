with open("D:\\Programowanie\\Repo\\AOC\\2024\\data24_2.txt", "r") as file:
    data = file.read().strip().split("\n")


def adv2_2(data):

    # chcecking conditions for new list
    def checking_report(report):
        trend = 0
        for level in range(len(report)):
            if level + 1 < len(report):
                a = report[level]
                b = report[level + 1]
                flag = True
                if a < b and 1 <= b - a <= 3 and (trend == 0 or trend == 1):
                    trend = 1
                    continue
                elif a > b and 1 <= a - b <= 3 and (trend == 0 or trend == 2):
                    trend = 2
                    continue
                else:
                    flag = False
                    break
        return flag

    flag = bool
    counter = 0
    for report in data:
        # converting reports into list of numbers
        report = report.split()
        report = [int(i) for i in report]
        trend = 0
        index = 0
        removed_element = 0
        removed_index = 0
        # checking conditions for base list
        for level in range(len(report)):
            if level + 1 < len(report):
                a = report[level]
                b = report[level + 1]
                flag = True
                if a < b and 1 <= b - a <= 3 and (trend == 0 or trend == 1):
                    trend = 1
                    index += 1
                    continue
                elif a > b and 1 <= a - b <= 3 and (trend == 0 or trend == 2):
                    trend = 2
                    index += 1
                    continue
                else:
                    if level + 1 < len(report):
                        # making 3 new lists without index, index+1 and index-1
                        report1 = report.copy()
                        del report1[index]
                        report2 = report.copy()
                        del report2[index + 1]
                        report3 = report.copy()
                        del report3[index - 1]
                        # checking conditions for every list
                        if checking_report(report1) == True:
                            break
                        elif checking_report(report2) == True:
                            break
                        elif checking_report(report3) == True:
                            break
                        else:
                            flag = False
                            break
                break
        # counting safe reports
        if flag == True:
            counter += 1
            flag = False

    return counter


def adv2_1(data):
    flag = bool
    counter = 0
    for report in data:
        # converting reports into list of numbers
        report = report.split()
        report = [int(i) for i in report]
        trend = 0
        # checking conditions
        for level in range(len(report)):
            if level + 1 < len(report):
                a = report[level]
                b = report[level + 1]
                flag = True
                if a < b and 1 <= b - a <= 3 and (trend == 0 or trend == 1):
                    trend = 1
                    continue
                elif a > b and 1 <= a - b <= 3 and (trend == 0 or trend == 2):
                    trend = 2
                    continue
                else:
                    flag = False
                    break
            else:
                break
        # counting safe reports
        if flag == True:
            counter += 1
            flag = False
    return counter


print(f"Wynik części pierwszej: {adv2_1(data)}\nWynik części drugiej: {adv2_2(data)}")
