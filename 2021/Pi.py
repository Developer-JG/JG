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


def Euler_2(value):
    n = 0
    while True:
        try:
            value += 1 / ((1 + 2 * n) ** 2)
            print("{:.256g}".format((value * 8) ** (1 / 2)))
            n += 1
        except:
            input("program is stoped")
            print("\n" * 2)
            main()


def Euler_3(value):
    n = 1
    while True:
        try:
            value += (((-1) ** (n + 1)) / (n ** 2))
            print("{:.256g}".format((value * 12) ** (1 / 2)))
            n += 1
        except:
            input("program is stoped")
            print("\n" * 2)
            main()


def Euler_prim(value):
    n = 2
    while True:
        try:
            if prime_number(n):
                value *= (n ** 2) / ((n ** 2) - 1)
        except:
            pass
        print(value)


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
    sel = input(" : ")

    if sel == '1':
        Ramanujan(value)
    elif sel == '2':
        Euler_3(value)
    elif sel == '3':
        Euler_2(value)


if __name__ == "__main__":
    main()