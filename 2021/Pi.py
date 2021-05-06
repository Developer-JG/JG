print("Pi project")


def factoriacl(number):
    result = 1
    for i in range(1 , number + 1):
        result *= i
    return result


def prime_number(number):
    if number != 1:
        for i in range(2,number):
            if number % i == 0:
                return False
    else:
        return False
    return True


def Franciscus_Vieta(value):
    value_1 = (2 ** (1 / 2))
    try:
        while True:
            value_1 += (2 + value) ** 1 / 2
            value_2 = value_1 / 2
            value *= value_2
            print("{:.256g}".format(value * (1 / 2)))
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def John_Wallis(value):
    n = 1
    try:
        while True:
            if value == 0:
                value += ((2 * n) / ((2 * n) - 1)) * ((2 * n) / ((2 * n) + 1))
            else:
                value *= ((2 * n) / ((2 * n) - 1)) * ((2 * n) / ((2 * n) + 1))
            print("{:.256g}".format(value * 2))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def James_Gregory_and_Leibniz(value):
    n = 0
    try:
        while True:
            value += ((-1) ** n) / ((2 * n) + 1)
            print("{:.256g}".format(value * 4))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def John_Machin(value):
    n = 1
    try:
        while True:
            value += (((4 * ((-1) ** (n - 1))) / ((2 * n) - 1)) * ((1 / 5) ** ((2 * n) - 1))) - \
                     (((-1) ** (n - 1)) / ((2 * n) - 1) * (1 / 239))
            print("{:.256g}".format((value * 4)))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def Euler_1(value):
    n = 1
    try:
        while True:
            value += 1 / (n ** 2)
            print("{:.256g}".format((value * 6) ** (1 / 2)))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def Euler_2(value):
    n = 0
    try:
        while True:
            value += 1 / ((1 + 2 * n) ** 2)
            print("{:.256g}".format((value * 8) ** (1 / 2)))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def Euler_3(value):
    n = 1
    try:
        while True:
            value += (((-1) ** (n + 1)) / (n ** 2))
            print("{:.256g}".format((value * 12) ** (1 / 2)))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def Euler_prim(value):
    n = 2
    try:
        while True:
            if prime_number(n) == True:
                if  value == 0:
                    value += ((n ** 2) / ((n ** 2) - 1))
                else:
                    value *= ((n ** 2) / ((n ** 2) - 1))
                print("{:.256g}".format(value))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def Ramanujan(value):
    n = 0
    try:
        while True:
            value_1 = factoriacl(4 * n) / factoriacl(n)
            value_2 = ((26390 * n) + 1103) / (396 ** (4 * n))
            value_0 = value_1 * value_2
            value += value_0
            print("{:.256g}".format(((2 * (2 ** (1 / 2))) / (99 ** 2) * value) ** -1))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def main():
    value = 0
    while True:
        sel = input(" : ")

        if sel == 'John_Wallis':
            John_Wallis(value)
        elif sel == 'James_Gregory_and_Leibniz':
            James_Gregory_and_Leibniz(value)
        elif sel == 'John_Machin':
            John_Machin(value)
        elif sel == 'Euler_1':
            Euler_1(value)
        if sel == 'Euler_2':
            Euler_2(value)
        elif sel == 'Euler_3':
            Euler_3(value)
        elif sel == 'Euler_prim':
            Euler_prim(value)
        elif sel == 'Ramanujan':
            Ramanujan(value)


if __name__ == "__main__":
    main()